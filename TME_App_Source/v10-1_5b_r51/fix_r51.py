# r5.1 rev 3 — base: TEST_1 = the Studio-Live TEST app (SHA-256 8744682d96e4ec46eb7694c7e0ef3b6c3a01f884f5eb2ed3f66cb64f92965641)
# Changes vs rev 2 (OpenClaw/Copilot review of rev 2, 2026-11-21):
#  * every acknowledged save is written to TWO slots ("C22PA/B/C" rotation): the slot holding the latest acknowledged copy
#    (varCountSlotKeepV22) is never touched while the next version is written; one corrupted slot can no longer lose a row.
#    If only one copy could be written the save still succeeds but warns (varCountSingleCopyV22).
#  * P is read from the newest valid slot only (no union across P slots) -> synced rows cannot come back from an older slot.
#  * old sources (C21, r5 "C22P") are merged once; a marker "C22M" written after a verified migration stops re-merging.
#  * unreadable C22H locks history writes for the session (old H never overwritten); per-source states decide cleanup.
#  * conflicts / rows of another owner -> integrity block: saving (Button1_2 + every device write) and uploading stop.
#  * read-back compares an extended signature (qty, date, opening, variance, reason, comment, archived, revision, synced, SP id);
#    P must contain only unsent rows, H only sent rows.
#  * varCountWindowStartV22 declared (commission start; blank = today-2); personal-report restore for warehouse-scoped users
#    windowed too; personal-report export blocked for periods older than the device window.
#  * all SaveData checks use IfError(SaveData(...);true,false) (perf log included).
# run from repo root: python3 TME_App_Source/v10-1_5b_r51/fix_r51.py <dir with props.py>
import os,sys,re
sys.path.insert(0,sys.argv[1]); from props import props
BASE='TME_App_Source/v10-1_5b_test1_studio/Src/'
B='TME_App_Source/v10-1_5b_r51/Src/'
OUT='TME_App_Source/v10-1_5b_r51/PASTE/'
def rd(fn): return open(B+fn,encoding='utf-8',newline='').read()
def wr(fn,s): open(B+fn,'w',encoding='utf-8',newline='').write(s)
FILES=[f for f in sorted(os.listdir(B)) if f.endswith('.pa.yaml') and not f.startswith('_')]
def glob(o,n,expect):
    tot=0
    for f in FILES:
        s=rd(f); c=s.count(o)
        if c: tot+=c; wr(f,s.replace(o,n))
    assert tot==expect,(o[:70],tot,expect)
def rep(s,o,n,c=1):
    assert s.count(o)==c,(o[:90],s.count(o)); return s.replace(o,n)
OID='Substitute(Text(User().EntraObjectId),"-","")'
WIN='Coalesce(varCountWindowStartV22,DateAdd(Today(),-Coalesce(varCountWindowDaysV22,2),TimeUnit.Days))'
UNSENT='CountRows(Filter(colOfflineInventory,!Synced))'
BLOCK='Coalesce(varCountIntegrityBlockV22,false)'
def SIG(p): return p+'ItemNo & "|" & '+p+'LocationCode & "|" & Text('+p+'CountQty) & "|" & Text('+p+'CountDate,"yyyymmddhhmmss") & "|" & '+p+'OwnerEmail'
def CSIG(p): return SIG(p)+' & "|" & Text('+p+'OpeningBalance) & "|" & '+p+'Reason & "|" & '+p+'Comment & "|" & Text('+p+'Archived)'
def VSIG(p): return CSIG(p)+' & "|" & Text('+p+'Variance) & "|" & Text('+p+'Revision) & "|" & Text('+p+'Synced) & "|" & Text('+p+'SharePointID)'
def ERR(msg): return 'Error({Kind:ErrorKind.Validation,Message:"'+msg+'"})'
CAND='SortByColumns(Filter(colCountSlotSeqV22,!Bad && Slot<>Coalesce(varCountSlotKeepV22,"")),"Seq",SortOrder.Ascending)'
def PATCHSLOT(slot,rec): return 'Patch(colCountSlotSeqV22,LookUp(colCountSlotSeqV22,Slot='+slot+'),'+rec+')'
PWRITE=('With({_p22:JSON(Filter(colOfflineInventory,!Synced),JSONFormat.Compact),_seq:Coalesce(varCountSeqV22,0)+1,'
 '_t1:First('+CAND+').Slot,_t2:Last(FirstN('+CAND+',2)).Slot},'
 'If(IsError(_p22) || Left(_p22,1)<>"[" || Right(_p22,1)<>"]",'+ERR('Тооллогын кэшийг бэлдэж чадсангүй. Хуучин файлыг дарж бичсэнгүй.')+','
 'CountRows(Filter(colOfflineInventory,!Synced && OwnerEmail<>varCountOwner))>0,'+ERR('Өөр хэрэглэгчийн илгээгээгүй мөр байна. Хадгалалтыг зогсоов; IT-д хандана уу.')+','
 +BLOCK+','+ERR('Төхөөрөмжийн кэшийн бүрэн бүтэн байдал баталгаажаагүй. Хадгалалтыг зогсоов; IT-д хандана уу.')+','
 'IsBlank(_t1),'+ERR('Төхөөрөмжийн нөөц файлууд бичигдэхгүй байна. Хуучин хуулбарыг хадгалж, шинээр бичсэнгүй.')+','
 'ClearCollect(colCountDiskV21,{Schema:22,Owner:varCountOwner,Payload:_p22,Seq:_seq});'
 'Set(varCountW1V22,IfError(SaveData(colCountDiskV21,"C22P" & _t1 & '+OID+');true,false));'
 'If(!varCountW1V22,'+PATCHSLOT('_t1','{Bad:true}')+');'
 'Set(varCountW2V22,_t2<>_t1 && IfError(SaveData(colCountDiskV21,"C22P" & _t2 & '+OID+');true,false));'
 'If(_t2<>_t1 && !varCountW2V22,'+PATCHSLOT('_t2','{Bad:true}')+');'
 'If(!varCountW1V22 && !varCountW2V22,'+ERR('Төхөөрөмжид бичиж чадсангүй. Оруулсан утга хадгалагдсангүй.')+','
 'Set(varCountSeqV22,_seq);If(varCountW1V22,'+PATCHSLOT('_t1','{Seq:_seq}')+');If(varCountW2V22,'+PATCHSLOT('_t2','{Seq:_seq}')+');'
 'Set(varCountSlotKeepV22,If(varCountW1V22,_t1,_t2));Set(varCountSingleCopyV22,!(varCountW1V22 && varCountW2V22)))))')
HSEL='FirstN(SortByColumns(Filter(colOfflineInventory,Synced),"CountDate",SortOrder.Descending),{n})'
HJSON=('If(IsEmpty(Filter(colOfflineInventory,Synced)),"[]",IfError(JSON('+HSEL.format(n=1000)+',JSONFormat.Compact),'
       'IfError(JSON('+HSEL.format(n=400)+',JSONFormat.Compact),JSON('+HSEL.format(n=100)+',JSONFormat.Compact))))')
HWRITE=('If(Coalesce(varCountHistLockV22,false) || '+BLOCK+',false,With({_h22:'+HJSON+'},If(IsError(_h22) || Left(_h22,1)<>"[" || Right(_h22,1)<>"]",'+ERR('Түүхийн кэшийг бэлдэж чадсангүй. Хуучин түүхийг үлдээв.')+','
        'ClearCollect(colCountHistDiskV22,{Schema:22,Owner:varCountOwner,Payload:_h22});'
        'If(IfError(SaveData(colCountHistDiskV22,"C22H" & '+OID+');true,false),Set(varCountHistDiskAtV22,Now()),'+ERR('Түүхийг төхөөрөмжид бичиж чадсангүй.')+'))))')
# ---- 1. device writes: 15 standard sites + Button1_2 append path (TEST_1)
tot=0
for f in FILES:
    t=rd(f)
    t,c=re.subn(r'ClearCollect\(colCountDiskV21,\{Schema:21,Owner:varCountOwner,Payload:JSON\(colOfflineInventory,JSONFormat\.Compact\)\}\);\s*SaveData\(colCountDiskV21,varCountCacheKey\)',lambda m:PWRITE,t)
    if c: tot+=c; wr(f,t)
assert tot==15,tot
s=rd('scrWarehouses.pa.yaml')
s,c=re.subn(r'If\(IsError\(With\(\{cache:First\(colCountDiskV21\)\},.*?SaveData\(colCountDiskV21,varCountCacheKey\)\)',lambda m:PWRITE,s,flags=re.S); assert c==1,c
# ---- 2. save button (the only place that creates count rows): integrity block, unsent-row limits, single-copy warning
s=rep(s,'IsBlank(varCountOwner) || varCountOwner<>Lower(Trim(User().Email)),Notify("Microsoft 365 хэрэглэгчийг шалгана уу.",NotificationType.Error),',
 'IsBlank(varCountOwner) || varCountOwner<>Lower(Trim(User().Email)),Notify("Microsoft 365 хэрэглэгчийг шалгана уу.",NotificationType.Error),'
 +BLOCK+',Notify("Төхөөрөмжийн тооллогын кэшид зөрчил илэрсэн. Мэдээллийг хамгаалж хадгалалт, илгээлтийг зогсоов. IT-д хандана уу.",NotificationType.Error,10000),'
 +UNSENT+'>=1200,Notify("Илгээгээгүй 1,200 тооллого хуримтлагдсан. Өгөгдөл алдагдахаас сэргийлж шинэ тооллогыг түр хаалаа. Сүлжээнд холбогдож илгээнэ үү.",NotificationType.Error,10000),')
s=rep(s,'Set(varCountLastSavedAtV21,Now());Set(varCountLastSavedQtyV21,_qty);',
 'Set(varCountLastSavedAtV21,Now());Set(varCountLastSavedQtyV21,_qty);'
 'If(Coalesce(varCountSingleCopyV22,false) && !varCountCloudOnlyV21,Notify("Тооллого хадгалагдсан ч төхөөрөмж дээр нэг л хуулбар үлдлээ. Сүлжээнд холбогдож илгээнэ үү.",NotificationType.Warning,4000));'
 'If('+UNSENT+'>=800,Notify("Илгээгээгүй " & '+UNSENT+' & " тооллого байна. 1,200 хүрэхэд шинэ тооллого хаагдана. Сүлжээнд холбогдож илгээнэ үү.",NotificationType.Warning,4000));')
s=rep(s,'!IsError(SaveData(colCountReceiptDiskV1015,"CountReceiptV1015_" & '+OID+'))','IfError(SaveData(colCountReceiptDiskV1015,"CountReceiptV1015_" & '+OID+');true,false)')
s=rep(s,'If(IsError(SaveData(colPerfSumV1015,k)),','If(!IfError(SaveData(colPerfSumV1015,k);true,false),')
wr('scrWarehouses.pa.yaml',s)
# ---- 3. SharePoint restores: window only (incl. warehouse-scoped personal report); after merge prune + persist H
glob("Filter(InventoryCount,Counter=varCountOwner || (Counter=User().FullName && 'Created By'.Email=varCountOwner))",
     "Filter(InventoryCount,(Counter=varCountOwner || (Counter=User().FullName && 'Created By'.Email=varCountOwner)) && Created>="+WIN+")",6)
glob("Filter(InventoryCount,LocationCode=w.Value && (Counter=varCountOwner || (Counter=User().FullName && 'Created By'.Email=varCountOwner)))",
     "Filter(InventoryCount,LocationCode=w.Value && (Counter=varCountOwner || (Counter=User().FullName && 'Created By'.Email=varCountOwner)) && Created>="+WIN+")",1)
glob('ClearCollect(colOfflineInventory,DropColumns(colHistoryMergedV16,MergePriority));',
     'ClearCollect(colOfflineInventory,DropColumns(colHistoryMergedV16,MergePriority));'
     'RemoveIf(colOfflineInventory,Synced && !IsBlank(CountDate) && CountDate<'+WIN+');'
     'If(varCountDiskSafeV21,IfError('+HWRITE+',Set(varCountHistDiskErrorV22,FirstError.Message)));',6)
# personal report export: refuse a period that starts before the device window (the device no longer holds those rows)
COV=('!IsBlank(varRptStart) && varRptStart<'+WIN+',Notify("Төхөөрөмж дээр зөвхөн " & Text('+WIN+',"yyyy-mm-dd") & "-аас хойшх тооллого байна. '
     'Дутуу тайлан илгээхгүй. Бүрэн тайланг Нэгдсэн тайлангаас авна уу.",NotificationType.Warning),')
s=rd('ScrReport1.pa.yaml')
s=rep(s,',varRptCloudLimit || varRInvalidDates,Notify(',','+COV+'varRptCloudLimit || varRInvalidDates,Notify(')
s=rep(s,'NotificationType.Warning),varRInvalidDates,Notify("Огнооны дарааллыг','NotificationType.Warning),'+COV+'varRInvalidDates,Notify("Огнооны дарааллыг')
wr('ScrReport1.pa.yaml',s)
# ---- 4. App.OnStart
s=rd('App.pa.yaml')
s=rep(s,'Set(varCountCacheKey,"C21" & '+OID+');',
 'Set(varCountCacheKey,"C22PA" & '+OID+');Set(varCountHistKeyV22,"C22H" & '+OID+');Set(varCountLegacyKeyV22,"C21" & '+OID+');'
 'Set(varCountWindowDaysV22,2);Set(varCountWindowStartV22,If(false,Today()));\n'
 '      // r5.1 TEST: old files are verified but NOT deleted. Production: true only after all device tests pass.\n'
 '      Set(varCountMigrateDeleteV22,false);'
 'Set(varCountMigrateV22,false);Set(varCountRewriteV22,false);Set(varCountHistDiskErrorV22,"");Set(varCountSeqV22,0);Set(varCountSlotErrV22,"");'
 'Set(varCountSlotKeepV22,"");Set(varCountSlotMainV22,"");Set(varCountSlotBlockV22,false);Set(varCountSingleCopyV22,false);Set(varCountW1V22,false);Set(varCountW2V22,false);'
 'Set(varCountMigrateConflictV22,0);Set(varCountForeignRowsV22,0);Set(varCountIntegrityBlockV22,false);Set(varCountHistLockV22,false);'
 'Set(varCountLegacyStateV22,"none");Set(varCountR5StateV22,"none");Set(varCountMigrateMarkV22,false);Set(varCountMigrateOkV22,false);Set(varCountMigrateStatusV22,"");'
 'ClearCollect(colCountHistDiskV22,{Schema:22,Owner:"",Payload:"[]"});Clear(colCountHistDiskV22);'
 'ClearCollect(colCountSlotSeqV22,{Slot:"A",Seq:-1,Bad:false},{Slot:"B",Seq:-1,Bad:false},{Slot:"C",Seq:-1,Bad:false});')
s=rep(s,'ClearCollect(colCountDiskV21,{Schema:21,Owner:"",Payload:"[]"});Clear(colCountDiskV21);',
        'ClearCollect(colCountDiskV21,{Schema:21,Owner:"",Payload:"[]",Seq:0});Clear(colCountDiskV21);')
mm=re.search(r'ClearCollect\(colOfflineInventory,ForAll\(Table\(ParseJSON\(First\(colCountDiskV21\)\.Payload\)\) As r,(\{.*?Synced:Boolean\(r\.Value\.Synced\)\})\)\)',s,re.S)
assert mm; MAP=mm.group(1)
def PARSE(payload): return 'ForAll(Table(ParseJSON('+payload+')) As r,'+MAP+')'
ROWERR='IsError(SyncKey) || IsBlank(SyncKey) || IsError(Synced) || IsError(OwnerEmail) || IsError(CountQty) || IsError(CountDate) || IsError(Revision) || IsError(ItemNo) || IsError(LocationCode)'
def LOADTRY(coll,key): return ('If(IfError(LoadData('+coll+','+key+',true);true,false),true,IfError(Clear('+coll+');LoadData('+coll+','+key+',true);true,false))')
# 4a. slots: read A/B/C/R5 (retry once); newest valid = main P; unreadable/invalid A/B/C = bad (never written); block only if none valid
ind='      '
def slot(key,tag):
    bad='' if tag=='R5' else ';'+PATCHSLOT('"'+tag+'"','{Bad:true}')
    return (ind+'Clear(colCountSlotTmpV22);If('+LOADTRY('colCountSlotTmpV22',key)+',Collect(colCountSlotV22,AddColumns(colCountSlotTmpV22,Slot,"'+tag+'")),'
            'Clear(colCountSlotTmpV22);Set(varCountSlotErrV22,varCountSlotErrV22 & "'+tag+' ")'+bad+');\n')
NEWEST='First(SortByColumns(AddColumns(colCountSlotOkV22,SeqN,Coalesce(Seq,0)),"SeqN",SortOrder.Descending))'
LOAD=(ind+'ClearCollect(colCountSlotTmpV22,{Schema:21,Owner:"",Payload:"[]",Seq:0});Clear(colCountSlotTmpV22);'
      'ClearCollect(colCountSlotV22,AddColumns(colCountSlotTmpV22,Slot,""));Clear(colCountSlotV22);\n'
      +slot('"C22PA" & '+OID,'A')+slot('"C22PB" & '+OID,'B')+slot('"C22PC" & '+OID,'C')+slot('"C22P" & '+OID,'R5')+
      ind+'ClearCollect(colCountSlotOkV22,Filter(colCountSlotV22,Schema=22 && Owner=varCountOwner && Left(Payload,1)="[" && Right(Payload,1)="]" && !IsError(ParseJSON(Payload))));\n'
      +ind+'ForAll(Filter(colCountSlotV22,Slot in ["A","B","C"] && !(Slot in colCountSlotOkV22.Slot)) As b,'+PATCHSLOT('b.Slot','{Bad:true}')+');\n'
      +ind+'ForAll(Filter(colCountSlotOkV22,Slot in ["A","B","C"]) As o,'+PATCHSLOT('o.Slot','{Seq:Coalesce(o.Seq,0)}')+');\n'
      +ind+'Set(varCountSlotBlockV22,IsEmpty(colCountSlotOkV22) && (!IsBlank(varCountSlotErrV22) || !IsEmpty(colCountSlotV22)));\n'
      +ind+'Set(varCountSlotMainV22,'+NEWEST+'.Slot);\n'
      +ind+'ClearCollect(colCountDiskV21,ShowColumns(Filter(colCountSlotOkV22,Slot=varCountSlotMainV22),Schema,Owner,Payload,Seq));\n'
      +ind+'Set(varCountSeqV22,Coalesce(Max(colCountSlotOkV22,Coalesce(Seq,0)),0));\n'
      +ind+'Set(varCountSlotKeepV22,If(varCountSlotMainV22 in ["A","B","C"],varCountSlotMainV22,""));\n'
      +ind+'If(varCountSlotMainV22="R5",Set(varCountR5StateV22,"ok"),!IsEmpty(Filter(colCountSlotV22,Slot="R5")) && IsEmpty(Filter(colCountSlotOkV22,Slot="R5")),Set(varCountR5StateV22,"bad"),'
      '"R5 " in varCountSlotErrV22,Set(varCountR5StateV22,"bad"));\n')
s=rep(s,'      If(IsError(LoadData(colCountDiskV21,varCountCacheKey,true)),\n',LOAD+'      If(varCountSlotBlockV22,\n')
s=rep(s,'CountRows(colCountDiskV21)<>1 || First(colCountDiskV21).Schema<>21 ||','CountRows(colCountDiskV21)<>1 || First(colCountDiskV21).Schema<>22 ||')
# 4b. after a safe load: H (lock if unreadable) + one-time merge of old sources (unless the migration marker exists)
I2='\n       '
def SRC(coll,key,rank,tag,state):
    st=(lambda v:'Set('+state+',"'+v+'")') if state else (lambda v:'Set(varCountHistLockV22,true)' if v=='bad' else 'true')
    return (I2+'ClearCollect('+coll+',{Schema:21,Owner:"",Payload:"[]",Seq:0});Clear('+coll+');'
     'If('+LOADTRY(coll,key)+','
     'If(!IsEmpty('+coll+'),If(CountRows('+coll+')<>1 || First('+coll+').Owner<>varCountOwner || IsError(ParseJSON(First('+coll+').Payload)),'
     +st('bad')+';Set(varCountHistDiskErrorV22,varCountHistDiskErrorV22 & "'+tag+' бүтэц таарахгүй; хадгалав. "),'
     'ClearCollect(colCountSrcRowsV22,'+PARSE('First('+coll+').Payload')+');'
     'If(CountIf(colCountSrcRowsV22,'+ROWERR+')>0,'+st('bad')+';Set(varCountHistDiskErrorV22,varCountHistDiskErrorV22 & "'+tag+' мөр уншигдсангүй; хадгалав. "),'
     'Collect(colCountAllV22,AddColumns(colCountSrcRowsV22,SrcRank,'+rank+'));'+st('ok')+');Clear(colCountSrcRowsV22))),'
     +st('bad')+';Set(varCountHistDiskErrorV22,varCountHistDiskErrorV22 & "'+tag+' уншигдсангүй; хадгалав. "));Clear('+coll+');')
UNION=(I2+'// r5.1: H + one-time merge of old sources by SyncKey (unreadable sources are skipped, kept and never overwritten)'
 +I2+'ClearCollect(colCountMarkV22,{Done:false,At:Now()});Clear(colCountMarkV22);'
 'If('+LOADTRY('colCountMarkV22','"C22M" & '+OID)+',Set(varCountMigrateMarkV22,!IsEmpty(colCountMarkV22) && First(colCountMarkV22).Done=true),Set(varCountMigrateMarkV22,false));Clear(colCountMarkV22);'
 +I2+'ClearCollect(colCountAllV22,AddColumns(colOfflineInventory,SrcRank,100));'
 +SRC('colCountHistDiskV22','varCountHistKeyV22','20','C22H','')
 +I2+'If(!varCountMigrateMarkV22,'
 'ForAll(Filter(colCountSlotOkV22,Slot="R5" && varCountSlotMainV22<>"R5") As o,Collect(colCountAllV22,AddColumns('+PARSE('o.Payload')+',SrcRank,30)));'
 'If(!IsEmpty(Filter(colCountSlotOkV22,Slot="R5")),Set(varCountR5StateV22,"ok")));'
 +I2+'If(!varCountMigrateMarkV22,'+SRC('colCountLegacyDiskV22','varCountLegacyKeyV22','10','C21','varCountLegacyStateV22')[:-1]+I2+');'
 +I2+'Set(varCountMigrateV22,!varCountMigrateMarkV22 && (varCountLegacyStateV22="ok" || varCountR5StateV22="ok"));'
 +I2+'Set(varCountForeignRowsV22,CountRows(Filter(colCountAllV22,OwnerEmail<>varCountOwner)));'
 +I2+'ClearCollect(colCountAll2V22,AddColumns(Filter(colCountAllV22,OwnerEmail=varCountOwner),SyncedN,If(Synced,1,0),RevN,Coalesce(Revision,0)));Clear(colCountAllV22);'
 +I2+'Set(varCountMigrateConflictV22,CountRows(Filter(ForAll(GroupBy(colCountAll2V22,SyncKey,G) As g,'
 '{n:CountRows(Distinct(Filter(g.G,RevN=Max(g.G,RevN)),'+CSIG('')+'))}),n>1)));'
 +I2+'ClearCollect(colCountWinV22,ForAll(GroupBy(colCountAll2V22,SyncKey,G) As g,'
 'Patch(First(SortByColumns(g.G,"RevN",SortOrder.Descending,"SyncedN",SortOrder.Descending,"SrcRank",SortOrder.Descending)),{SyncKey:g.SyncKey})));'
 +I2+'Set(varCountRewriteV22,!IsEmpty(Filter(colCountWinV22,!Synced && SrcRank<100)) || CountRows(Filter(colCountWinV22,!Synced))<>CountRows(Filter(colOfflineInventory,!Synced)));'
 +I2+'ClearCollect(colOfflineInventory,DropColumns(colCountWinV22,SrcRank,SyncedN,RevN));Clear(colCountAll2V22);Clear(colCountWinV22);'
 +I2+'Set(varCountIntegrityBlockV22,varCountForeignRowsV22>0 || varCountMigrateConflictV22>0);'
 +I2+'If(varCountIntegrityBlockV22,Set(varCountDiskSafeV21,false);Set(varCountCacheReady,false);Set(varCountStorageError,"Төхөөрөмжийн кэшид "'
 ' & If(varCountForeignRowsV22>0,"өөр хэрэглэгчийн " & varCountForeignRowsV22 & " мөр ","") & If(varCountMigrateConflictV22>0,varCountMigrateConflictV22 & " зөрчилтэй мөр ","") & "илэрлээ. Файлуудыг хадгалж, хадгалалт/илгээлтийг зогсоов. IT-д хандана уу."));'
 +I2+'RemoveIf(colOfflineInventory,Synced && !IsBlank(CountDate) && CountDate<'+WIN+')\n')
GUARD=('\n      // r5.1: P slots exist but none is valid -> unsafe (nothing is overwritten)\n'
 '      If(varCountSlotBlockV22,Set(varCountDiskSafeV21,false);Set(varCountLoadErrorV21,true);'
 'Set(varCountStorageError,"Төхөөрөмжийн тооллогын файлыг уншиж чадсангүй. Хуучин файлыг дарж бичихгүй."));')
s=rep(s,'\n      If(varCountDiskSafeV21,\n       // v3.6.8: set-based merge',GUARD+'\n      If(varCountDiskSafeV21,'+UNION+'      );\n      If(varCountDiskSafeV21,\n       // v3.6.8: set-based merge')
s=rep(s,'If(varPerfPrevCandidatesV368=0 && !IsEmpty(colCountDiskV21),Set(varCountCacheReady,true)',
        'If(varPerfPrevCandidatesV368=0 && !IsEmpty(colCountDiskV21) && !varCountMigrateV22 && !varCountRewriteV22 && !'+BLOCK+',Set(varCountCacheReady,true)')
# 4c. migration: write P+H, read back the kept P slot and H, compare extended signatures both ways; then marker; then (if enabled) delete only fully read sources
VKEY='v.SyncKey=p.SyncKey && '+VSIG('v.')+'='+VSIG('p.')
def READ(key): return ('ClearCollect(colCountVerifyV22,{Schema:22,Owner:"",Payload:"[]",Seq:0});Clear(colCountVerifyV22);LoadData(colCountVerifyV22,'+key+',true);'
                      'ClearCollect(colCountVerifyRowsV22,'+PARSE('First(colCountVerifyV22).Payload')+')')
NSYNC='CountRows(Filter(colOfflineInventory,Synced))'
FIN=('      RemoveIf(colOfflineInventory,Synced && !IsBlank(CountDate) && CountDate<'+WIN+');\n'
 '      // r5.1: old files are retired only after P and H were written, read back and matched row by row\n'
 '      If(varCountMigrateV22 && varCountDiskSafeV21 && varCountCacheReady && !'+BLOCK+' && !varCountHistLockV22,\n'
 '       Set(varCountMigrateOkV22,false);\n'
 '       IfError(\n'
 '        '+PWRITE+';\n'
 '        '+HWRITE+';\n'
 '        '+READ('"C22P" & varCountSlotKeepV22 & '+OID)+';\n'
 '        ClearCollect(colCountVerifyPendV22,Filter(colOfflineInventory,!Synced));\n'
 '        Set(varCountMigrateOkV22,!IsBlank(varCountSlotKeepV22) && CountRows(colCountVerifyV22)=1 && First(colCountVerifyV22).Schema=22 && First(colCountVerifyV22).Owner=varCountOwner && '
 'First(colCountVerifyV22).Seq=varCountSeqV22 && CountIf(colCountVerifyRowsV22,Synced)=0 && CountRows(colCountVerifyRowsV22)=CountRows(colCountVerifyPendV22) && '
 'CountRows(Distinct(colCountVerifyRowsV22,SyncKey))=CountRows(colCountVerifyRowsV22) && '
 'CountRows(Filter(colCountVerifyPendV22 As p,IsBlank(LookUp(colCountVerifyRowsV22 As v,'+VKEY+').SyncKey)))=0);\n'
 '        '+READ('varCountHistKeyV22')+';\n'
 '        Set(varCountMigrateOkV22,varCountMigrateOkV22 && CountRows(colCountVerifyV22)=1 && First(colCountVerifyV22).Schema=22 && First(colCountVerifyV22).Owner=varCountOwner && '
 'CountIf(colCountVerifyRowsV22,!Synced)=0 && '
 'CountRows(colCountVerifyRowsV22) in [Min(1000,'+NSYNC+'),Min(400,'+NSYNC+'),Min(100,'+NSYNC+')] && '
 'CountRows(Distinct(colCountVerifyRowsV22,SyncKey))=CountRows(colCountVerifyRowsV22) && '
 'CountRows(Filter(colCountVerifyRowsV22 As v,IsBlank(LookUp(colOfflineInventory As p,p.Synced && '+VKEY+').SyncKey)))=0 && '
 'CountRows(Filter(FirstN(SortByColumns(Filter(colOfflineInventory,Synced),"CountDate",SortOrder.Descending),CountRows(colCountVerifyRowsV22)) As p,IsBlank(LookUp(colCountVerifyRowsV22 As v,'+VKEY+').SyncKey)))=0);\n'
 '        true,Set(varCountMigrateOkV22,false));\n'
 '       If(varCountMigrateOkV22 && varCountLegacyStateV22<>"bad" && varCountR5StateV22<>"bad",\n'
 '        ClearCollect(colCountMarkV22,{Done:true,At:Now()});Set(varCountMigrateMarkV22,IfError(SaveData(colCountMarkV22,"C22M" & '+OID+');true,false));Clear(colCountMarkV22));\n'
 '       If(varCountMigrateOkV22 && varCountMigrateDeleteV22,\n'
 '        If(varCountLegacyStateV22="ok",IfError(ClearData(varCountLegacyKeyV22);true,false));\n'
 '        If(varCountR5StateV22="ok",IfError(ClearData("C22P" & '+OID+');true,false));\n'
 '        Set(varCountMigrateStatusV22,"verified, fully read sources deleted"),\n'
 '        varCountMigrateOkV22,Set(varCountMigrateStatusV22,"verified, delete disabled"),\n'
 '        Set(varCountMigrateStatusV22,"not verified, old files kept"));\n'
 '       Clear(colCountVerifyV22);Clear(colCountVerifyRowsV22);Clear(colCountVerifyPendV22));\n'
 '      If('+BLOCK+' || !IsBlank(varCountSlotErrV22) || !IsBlank(varCountHistDiskErrorV22),Notify("Төхөөрөмжийн кэш: " & '
 'If('+BLOCK+',varCountStorageError & " ","") & If(!IsBlank(varCountSlotErrV22),"уншигдаагүй хуулбар: " & varCountSlotErrV22 & "(бусдаас сэргээв). ","") & varCountHistDiskErrorV22,'
 'If('+BLOCK+',NotificationType.Error,NotificationType.Warning)));\n'
 '      Clear(colCountSlotV22);Clear(colCountSlotOkV22);Clear(colCountSlotTmpV22);\n')
s=rep(s,'Clear(colPreviousCountV21);\n      Set(varCountLoadDoneV21,true);','Clear(colPreviousCountV21);\n'+FIN+'      Set(varCountLoadDoneV21,true);')
wr('App.pa.yaml',s)
# ---- 5. upload timers: when the queue is empty, persist H at most every 10 minutes
def append_prop(fn,ctl,prop,suffix):
    L=rd(fn).split('\n')
    ci=next(i for i,l in enumerate(L) if l.strip()=='- '+ctl+':')
    ind0=len(L[ci])-len(L[ci].lstrip())
    pi=next(i for i in range(ci+1,len(L)) if L[i].strip().startswith(prop+':'))
    assert all((len(L[i])-len(L[i].lstrip())>ind0) for i in range(ci+1,pi+1)),'left control'
    pind=len(L[pi])-len(L[pi].lstrip()); last=pi
    if L[pi].strip().endswith('|-'):
        j=pi+1
        while j<len(L) and (L[j].strip()=='' or len(L[j])-len(L[j].lstrip())>pind): j+=1
        last=j-1
        while L[last].strip()=='': last-=1
    assert '//' not in L[last],(fn,ctl,'comment on last line')
    L[last]=L[last]+suffix; wr(fn,'\n'.join(L))
TSUF=(';If((IsBlank(varCountHistDiskAtV22) || varCountHistDiskAtV22<DateAdd(Now(),-10,TimeUnit.Minutes)) && '
      'varCountDiskSafeV21 && varCountCacheReady && IsEmpty(Filter(colOfflineInventory,!Synced)),'
      'IfError('+HWRITE+',Set(varCountHistDiskErrorV22,FirstError.Message)))')
for fn,ctl in [('ScrCountHome.pa.yaml','uploadQueueV16_10'),('нүүр.pa.yaml','uploadQueueV16_11'),('ScrHistory.pa.yaml','uploadQueueV16_12')]:
    append_prop(fn,ctl,'OnTimerEnd',TSUF)
# ---- checks + PASTE
def bal(f):
    f=re.sub(r'//[^\n]*','',f); f=re.sub(r'"[^"]*"','""',f); f=re.sub(r"'[^']*'","''",f); return (f.count('(')-f.count(')'),f.count('{')-f.count('}'))
tc=lambda x:len(re.findall(r';\s*\)',re.sub(r'//[^\n]*','',re.sub(r'"[^"]*"','""',x or ''))))
n=0
for fn in FILES:
    a=props(open(BASE+fn,encoding='utf-8').read()); b=props(rd(fn))
    for key in b:
        if a.get(key)!=b[key]:
            assert bal(b[key])==(bal(a[key]) if key in a else (0,0)),(key,bal(b[key])); assert tc(b[key])<=tc(a.get(key)),(key,'new trailing ;')
            n+=1; ctl,prop=key.rsplit('.',1)
            open(f'{OUT}{n:02d}_{fn[:-8]}_{ctl}_{prop}.txt','w',encoding='utf-8').write(b[key][1:]); print(n,key,len(b[key]))
allsrc=''.join(rd(f) for f in FILES)
print('full-table JSON:',allsrc.count('JSON(colOfflineInventory,'),'| old key writes:',allsrc.count('SaveData(colCountDiskV21,varCountCacheKey)'),
      '| IsError(SaveData:',allsrc.count('IsError(SaveData('),'| append path:',allsrc.count('{cache:First(colCountDiskV21)}'))
