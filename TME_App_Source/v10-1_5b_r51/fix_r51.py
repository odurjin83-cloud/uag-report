# r5.1 rev 4 — base: TEST_1 = Studio-Live TEST (SHA-256 8744682d96e4ec46eb7694c7e0ef3b6c3a01f884f5eb2ed3f66cb64f92965641)
# Rev 4 answers the independent review of rev 3 (2026-11-22, commit d4545b6):
#  1 "saved" only after BOTH copies were written. Five P slots "C22PA..E" + commit marker "C22PK".
#    A version is COMMITTED if it has >=2 valid identical copies, or it is the marker's Seq and >=1 valid copy exists.
#    Load uses the highest committed version; uncommitted single copies (torn/partial saves) are ignored.
#    A slot is valid only if every row parses with the right types. Two valid copies of the committed Seq that differ
#    -> integrity block. Marker says a Seq that has no valid copy -> unsafe (nothing overwritten).
#    The two slots of the committed version are never written; the next version goes to the two lowest other slots.
#    Seq is consumed even on a failed save (no ties). A failed save keeps its SyncKey for the retry of the same input.
#  2 Integrity block now guards EVERY SharePoint write path: all 9 properties containing Patch(InventoryCount ...)
#    are wrapped (buttons: message; timers: no-op), besides the device-write and new-count guards.
#  3 Migration marker "C22M" also stops the legacy V19 (InventoryV19_) merge; an unreadable marker = migration done
#    (never re-merge automatically).
#  * conflict / read-back signatures are JSON records (no delimiter ambiguity), incl. Variance and Resolved.
#  * migration cleanup steps are separate (each with its own success flag); delete status reflects ClearData results.
#  * personal-report export: blocked when the period starts before what the device actually holds
#    (window, or the oldest row of a capped history file) or when the last cloud refresh failed.
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
COVER='Coalesce(varCountCoverageFromV22,'+WIN+')'
UNSENT='CountRows(Filter(colOfflineInventory,!Synced))'
BLOCK='Coalesce(varCountIntegrityBlockV22,false)'
SLOTS='["A","B","C","D","E"]'
def CSIG(p): return ('JSON({i:'+p+'ItemNo,l:'+p+'LocationCode,q:'+p+'CountQty,d:'+p+'CountDate,o:'+p+'OwnerEmail,b:'+p+'OpeningBalance,'
                     'v:'+p+'Variance,r:'+p+'Reason,c:'+p+'Comment,a:'+p+'Archived,x:'+p+'Resolved},JSONFormat.Compact)')
def VSIG(p): return ('JSON({i:'+p+'ItemNo,l:'+p+'LocationCode,q:'+p+'CountQty,d:'+p+'CountDate,o:'+p+'OwnerEmail,b:'+p+'OpeningBalance,'
                     'v:'+p+'Variance,r:'+p+'Reason,c:'+p+'Comment,a:'+p+'Archived,x:'+p+'Resolved,n:'+p+'Revision,s:'+p+'Synced,p:'+p+'SharePointID},JSONFormat.Compact)')
def ERR(msg): return 'Error({Kind:ErrorKind.Validation,Message:"'+msg+'"})'
def PATCHSLOT(slot,rec): return 'Patch(colCountSlotSeqV22,LookUp(colCountSlotSeqV22,Slot='+slot+'),'+rec+')'
CAND='SortByColumns(Filter(colCountSlotSeqV22,!Bad && !("|" & Slot & "|" in Coalesce(varCountSlotKeepV22,""))),"Seq",SortOrder.Ascending)'
PWRITE=('With({_p22:JSON(Filter(colOfflineInventory,!Synced),JSONFormat.Compact),_seq:Coalesce(varCountSeqV22,0)+1,'
 '_t1:First('+CAND+').Slot,_t2:Last(FirstN('+CAND+',2)).Slot},'
 'If(IsError(_p22) || Left(_p22,1)<>"[" || Right(_p22,1)<>"]",'+ERR('Тооллогын кэшийг бэлдэж чадсангүй. Хуучин файлыг дарж бичсэнгүй.')+','
 'CountRows(Filter(colOfflineInventory,!Synced && OwnerEmail<>varCountOwner))>0,'+ERR('Өөр хэрэглэгчийн илгээгээгүй мөр байна. Хадгалалтыг зогсоов; IT-д хандана уу.')+','
 +BLOCK+','+ERR('Төхөөрөмжийн кэшийн бүрэн бүтэн байдал баталгаажаагүй. Хадгалалтыг зогсоов; IT-д хандана уу.')+','
 'IsBlank(_t1) || IsBlank(_t2) || _t1=_t2,'+ERR('Төхөөрөмжийн нөөц файл хүрэлцэхгүй байна. Хоёр хуулбар бичих боломжгүй тул хадгалсангүй.')+','
 'ClearCollect(colCountDiskV21,{Schema:22,Owner:varCountOwner,Payload:_p22,Seq:_seq});Set(varCountSeqV22,_seq);'
 'Set(varCountW1V22,IfError(SaveData(colCountDiskV21,"C22P" & _t1 & '+OID+');true,false));'
 'If(varCountW1V22,'+PATCHSLOT('_t1','{Seq:_seq}')+','+PATCHSLOT('_t1','{Bad:true}')+');'
 'Set(varCountW2V22,varCountW1V22 && IfError(SaveData(colCountDiskV21,"C22P" & _t2 & '+OID+');true,false));'
 'If(varCountW2V22,'+PATCHSLOT('_t2','{Seq:_seq}')+',If(varCountW1V22,'+PATCHSLOT('_t2','{Bad:true}')+'));'
 'If(!varCountW2V22,'+ERR('Төхөөрөмжид хоёр хуулбараар бичиж чадсангүй. Тооллого хадгалагдсангүй; дахин хадгална уу.')+','
 'Set(varCountSlotKeepV22,"|" & _t1 & "|" & _t2 & "|");'
 'ClearCollect(colCountMarkPV22,{Schema:22,Owner:varCountOwner,Seq:_seq});'
 'Set(varCountMarkOkV22,IfError(SaveData(colCountMarkPV22,"C22PK" & '+OID+');true,false)))))')
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
# ---- 2. save button: integrity block, unsent limits, retry keeps the SyncKey of a failed save of the same input
RSIG='varItem.number & "|" & varLocationCode & "|" & txtCountQty_2.Text'
s=rep(s,'IsBlank(varCountOwner) || varCountOwner<>Lower(Trim(User().Email)),Notify("Microsoft 365 хэрэглэгчийг шалгана уу.",NotificationType.Error),',
 'IsBlank(varCountOwner) || varCountOwner<>Lower(Trim(User().Email)),Notify("Microsoft 365 хэрэглэгчийг шалгана уу.",NotificationType.Error),'
 +BLOCK+',Notify("Төхөөрөмжийн тооллогын кэшид зөрчил илэрсэн. Мэдээллийг хамгаалж хадгалалт, илгээлтийг зогсоов. IT-д хандана уу.",NotificationType.Error,10000),'
 +UNSENT+'>=1200,Notify("Илгээгээгүй 1,200 тооллого хуримтлагдсан. Өгөгдөл алдагдахаас сэргийлж шинэ тооллогыг түр хаалаа. Сүлжээнд холбогдож илгээнэ үү.",NotificationType.Error,10000),')
s=rep(s,'Set(varCountAttemptKeyV21,Text(GUID()));',
 'Set(varCountAttemptKeyV21,If(!IsBlank(varCountRetryKeyV22) && varCountRetrySigV22='+RSIG+',varCountRetryKeyV22,Text(GUID())));')
s=rep(s,'RemoveIf(colOfflineInventory,SyncKey=_key);',
 'RemoveIf(colOfflineInventory,SyncKey=_key);Set(varCountRetryKeyV22,_key);Set(varCountRetrySigV22,'+RSIG+');')
s=rep(s,'Set(varCountLastSavedAtV21,Now());Set(varCountLastSavedQtyV21,_qty);',
 'Set(varCountLastSavedAtV21,Now());Set(varCountLastSavedQtyV21,_qty);Set(varCountRetryKeyV22,Blank());Set(varCountRetrySigV22,"");'
 'If('+UNSENT+'>=800,Notify("Илгээгээгүй " & '+UNSENT+' & " тооллого байна. 1,200 хүрэхэд шинэ тооллого хаагдана. Сүлжээнд холбогдож илгээнэ үү.",NotificationType.Warning,4000));')
s=rep(s,'!IsError(SaveData(colCountReceiptDiskV1015,"CountReceiptV1015_" & '+OID+'))','IfError(SaveData(colCountReceiptDiskV1015,"CountReceiptV1015_" & '+OID+');true,false)')
s=rep(s,'If(IsError(SaveData(colPerfSumV1015,k)),','If(!IfError(SaveData(colPerfSumV1015,k);true,false),')
wr('scrWarehouses.pa.yaml',s)
# ---- 3. SharePoint restores: window only; after merge prune + persist H; a successful restore covers the whole window
glob("Filter(InventoryCount,Counter=varCountOwner || (Counter=User().FullName && 'Created By'.Email=varCountOwner))",
     "Filter(InventoryCount,(Counter=varCountOwner || (Counter=User().FullName && 'Created By'.Email=varCountOwner)) && Created>="+WIN+")",6)
glob("Filter(InventoryCount,LocationCode=w.Value && (Counter=varCountOwner || (Counter=User().FullName && 'Created By'.Email=varCountOwner)))",
     "Filter(InventoryCount,LocationCode=w.Value && (Counter=varCountOwner || (Counter=User().FullName && 'Created By'.Email=varCountOwner)) && Created>="+WIN+")",1)
glob('ClearCollect(colOfflineInventory,DropColumns(colHistoryMergedV16,MergePriority));',
     'ClearCollect(colOfflineInventory,DropColumns(colHistoryMergedV16,MergePriority));'
     'RemoveIf(colOfflineInventory,Synced && !IsBlank(CountDate) && CountDate<'+WIN+');Set(varCountCoverageFromV22,'+WIN+');'
     'If(varCountDiskSafeV21,IfError('+HWRITE+',Set(varCountHistDiskErrorV22,FirstError.Message)));',6)
COV=('!IsBlank(varRptStart) && (varRptStart<'+COVER+' || Coalesce(varRptCloudError,false)),Notify("Төхөөрөмж дээр зөвхөн " & Text('+COVER+',"yyyy-mm-dd hh:mm") & "-аас хойшх тооллого бүрэн байна'
     ' (эсвэл сүүлийн шинэчлэлт амжилтгүй). Дутуу тайлан илгээхгүй. Бүрэн тайланг Нэгдсэн тайлангаас авна уу.",NotificationType.Warning),')
s=rd('ScrReport1.pa.yaml')
s=rep(s,',varRptCloudLimit || varRInvalidDates,Notify(',','+COV+'varRptCloudLimit || varRInvalidDates,Notify(')
s=rep(s,'NotificationType.Warning),varRInvalidDates,Notify("Огнооны дарааллыг','NotificationType.Warning),'+COV+'varRInvalidDates,Notify("Огнооны дарааллыг')
wr('ScrReport1.pa.yaml',s)
# ---- 4. App.OnStart
s=rd('App.pa.yaml')
s=rep(s,'Set(varCountCacheKey,"C21" & '+OID+');',
 'Set(varCountCacheKey,"C22PA" & '+OID+');Set(varCountHistKeyV22,"C22H" & '+OID+');Set(varCountLegacyKeyV22,"C21" & '+OID+');'
 'Set(varCountWindowDaysV22,2);Set(varCountWindowStartV22,If(false,Today()));Set(varCountCoverageFromV22,If(false,Now()));\n'
 '      // r5.1 TEST: old files are verified but NOT deleted. Production: true only after all device tests pass.\n'
 '      Set(varCountMigrateDeleteV22,false);'
 'Set(varCountMigrateV22,false);Set(varCountRewriteV22,false);Set(varCountHistDiskErrorV22,"");Set(varCountSeqV22,0);Set(varCountSlotErrV22,"");'
 'Set(varCountSlotKeepV22,"");Set(varCountSlotMainV22,"");Set(varCountSlotBlockV22,false);Set(varCountSlotSplitV22,false);Set(varCountW1V22,false);Set(varCountW2V22,false);'
 'Set(varCountMarkSeqV22,-1);Set(varCountCommitSeqV22,-1);Set(varCountMarkOkV22,false);Set(varCountRetryKeyV22,"");Set(varCountRetrySigV22,"");'
 'Set(varCountMigrateConflictV22,0);Set(varCountForeignRowsV22,0);Set(varCountIntegrityBlockV22,false);Set(varCountHistLockV22,false);Set(varCountHistNV22,0);'
 'Set(varCountLegacyStateV22,"none");Set(varCountR5StateV22,"none");Set(varCountMigrateMarkV22,false);Set(varCountMigrateOkV22,false);Set(varCountMigrateStatusV22,"");'
 'ClearCollect(colCountHistDiskV22,{Schema:22,Owner:"",Payload:"[]"});Clear(colCountHistDiskV22);'
 'ClearCollect(colCountMarkPV22,{Schema:22,Owner:"",Seq:0});Clear(colCountMarkPV22);'
 'ClearCollect(colCountSlotSeqV22,{Slot:"A",Seq:-1,Bad:false},{Slot:"B",Seq:-1,Bad:false},{Slot:"C",Seq:-1,Bad:false},{Slot:"D",Seq:-1,Bad:false},{Slot:"E",Seq:-1,Bad:false});')
s=rep(s,'ClearCollect(colCountDiskV21,{Schema:21,Owner:"",Payload:"[]"});Clear(colCountDiskV21);',
        'ClearCollect(colCountDiskV21,{Schema:21,Owner:"",Payload:"[]",Seq:0});Clear(colCountDiskV21);')
mm=re.search(r'ClearCollect\(colOfflineInventory,ForAll\(Table\(ParseJSON\(First\(colCountDiskV21\)\.Payload\)\) As r,(\{.*?Synced:Boolean\(r\.Value\.Synced\)\})\)\)',s,re.S)
assert mm; MAP=mm.group(1)
def PARSE(payload): return 'ForAll(Table(ParseJSON('+payload+')) As r,'+MAP+')'
ROWERR=('IsError(SyncKey) || IsBlank(SyncKey) || IsError(Synced) || IsError(OwnerEmail) || IsError(CountQty) || IsError(CountDate) || IsError(Revision) || '
        'IsError(ItemNo) || IsError(LocationCode) || IsError(OpeningBalance) || IsError(Variance) || IsError(Archived) || IsError(SharePointID) || IsError(Resolved)')
def LOADTRY(coll,key): return ('If(IfError(LoadData('+coll+','+key+',true);true,false),true,IfError(Clear('+coll+');LoadData('+coll+','+key+',true);true,false))')
ind='      '
def slot(key,tag):
    bad='' if tag=='R5' else ';'+PATCHSLOT('"'+tag+'"','{Bad:true}')
    return (ind+'Clear(colCountSlotTmpV22);If('+LOADTRY('colCountSlotTmpV22',key)+',Collect(colCountSlotV22,AddColumns(colCountSlotTmpV22,Slot,"'+tag+'")),'
            'Clear(colCountSlotTmpV22);Set(varCountSlotErrV22,varCountSlotErrV22 & "'+tag+' ")'+bad+');\n')
CMT='Filter(colCountSlotOkV22,Slot in '+SLOTS+' && Coalesce(Seq,0)=varCountCommitSeqV22)'
LOAD=(ind+'ClearCollect(colCountSlotTmpV22,{Schema:21,Owner:"",Payload:"[]",Seq:0});Clear(colCountSlotTmpV22);'
      'ClearCollect(colCountSlotV22,AddColumns(colCountSlotTmpV22,Slot,""));Clear(colCountSlotV22);\n'
      +''.join(slot('"C22P'+t+'" & '+OID,t) for t in 'ABCDE')+slot('"C22P" & '+OID,'R5')
      # valid = envelope ok AND every row parses with the right types
      +ind+'ClearCollect(colCountSlotOkV22,Filter(AddColumns(Filter(colCountSlotV22,Schema=22 && Owner=varCountOwner && Left(Payload,1)="[" && Right(Payload,1)="]" && !IsError(ParseJSON(Payload))),'
      'RowErr,IfError(CountIf('+PARSE('Payload')+','+ROWERR+'),1)),RowErr=0));\n'
      +ind+'ForAll(Filter(colCountSlotV22,Slot in '+SLOTS+' && !(Slot in colCountSlotOkV22.Slot)) As b,'+PATCHSLOT('b.Slot','{Bad:true}')+');\n'
      +ind+'ForAll(Filter(colCountSlotOkV22,Slot in '+SLOTS+') As o,'+PATCHSLOT('o.Slot','{Seq:Coalesce(o.Seq,0)}')+');\n'
      +ind+'If('+LOADTRY('colCountMarkPV22','"C22PK" & '+OID)+' && CountRows(colCountMarkPV22)=1 && First(colCountMarkPV22).Owner=varCountOwner,'
      'Set(varCountMarkSeqV22,Coalesce(First(colCountMarkPV22).Seq,-1)),Set(varCountMarkSeqV22,-1));Clear(colCountMarkPV22);\n'
      +ind+'ClearCollect(colCountSeqStatV22,ForAll(GroupBy(AddColumns(Filter(colCountSlotOkV22,Slot in '+SLOTS+'),SeqN,Coalesce(Seq,0)),SeqN,G) As g,'
      '{SeqN:g.SeqN,N:CountRows(g.G),D:CountRows(Distinct(g.G,Payload))}));\n'
      +ind+'Set(varCountCommitSeqV22,Coalesce(Max(Filter(colCountSeqStatV22,N>=2 || SeqN=varCountMarkSeqV22),SeqN),-1));\n'
      +ind+'Set(varCountSlotSplitV22,Coalesce(LookUp(colCountSeqStatV22,SeqN=varCountCommitSeqV22).D,0)>1);\n'
      +ind+'Set(varCountSlotMainV22,If(varCountCommitSeqV22>=0,First('+CMT+').Slot,!IsEmpty(Filter(colCountSlotOkV22,Slot="R5")),"R5",""));\n'
      +ind+'ClearCollect(colCountDiskV21,ShowColumns(Filter(colCountSlotOkV22,Slot=varCountSlotMainV22),Schema,Owner,Payload,Seq));\n'
      +ind+'Set(varCountSeqV22,Max(Coalesce(Max(colCountSlotOkV22,Coalesce(Seq,0)),0),varCountMarkSeqV22,0));\n'
      +ind+'Set(varCountSlotKeepV22,Concat('+CMT+',"|" & Slot) & "|");\n'
      # unsafe: the marker names a version that has no valid copy, or files exist/failed to load and nothing usable was found
      +ind+'Set(varCountSlotBlockV22,(varCountMarkSeqV22>varCountCommitSeqV22) || (IsBlank(varCountSlotMainV22) && (!IsBlank(varCountSlotErrV22) || !IsEmpty(Filter(colCountSlotV22,Slot in '+SLOTS+')))));\n'
      +ind+'If(varCountSlotMainV22="R5",Set(varCountR5StateV22,"ok"),!IsEmpty(Filter(colCountSlotV22,Slot="R5")) && IsEmpty(Filter(colCountSlotOkV22,Slot="R5")),Set(varCountR5StateV22,"bad"),'
      '"R5 " in varCountSlotErrV22,Set(varCountR5StateV22,"bad"));\n')
s=rep(s,'      If(IsError(LoadData(colCountDiskV21,varCountCacheKey,true)),\n',LOAD+'      If(varCountSlotBlockV22,\n')
s=rep(s,'CountRows(colCountDiskV21)<>1 || First(colCountDiskV21).Schema<>21 ||','CountRows(colCountDiskV21)<>1 || First(colCountDiskV21).Schema<>22 ||')
# 4b. after a safe load: H (lock if unreadable) + one-time merge of old sources unless the migration marker exists
I2='\n       '
def SRC(coll,key,rank,tag,state):
    st=(lambda v:'Set('+state+',"'+v+'")') if state else (lambda v:'Set(varCountHistLockV22,true)' if v=='bad' else 'Set(varCountHistNV22,CountRows(colCountSrcRowsV22));Set(varCountHistMinV22,Min(colCountSrcRowsV22,CountDate))')
    return (I2+'ClearCollect('+coll+',{Schema:21,Owner:"",Payload:"[]",Seq:0});Clear('+coll+');'
     'If('+LOADTRY(coll,key)+','
     'If(!IsEmpty('+coll+'),If(CountRows('+coll+')<>1 || First('+coll+').Owner<>varCountOwner || IsError(ParseJSON(First('+coll+').Payload)),'
     +st('bad')+';Set(varCountHistDiskErrorV22,varCountHistDiskErrorV22 & "'+tag+' бүтэц таарахгүй; хадгалав. "),'
     'ClearCollect(colCountSrcRowsV22,'+PARSE('First('+coll+').Payload')+');'
     'If(CountIf(colCountSrcRowsV22,'+ROWERR+')>0,'+st('bad')+';Set(varCountHistDiskErrorV22,varCountHistDiskErrorV22 & "'+tag+' мөр уншигдсангүй; хадгалав. "),'
     'Collect(colCountAllV22,AddColumns(colCountSrcRowsV22,SrcRank,'+rank+'));'+st('ok')+');Clear(colCountSrcRowsV22))),'
     +st('bad')+';Set(varCountHistDiskErrorV22,varCountHistDiskErrorV22 & "'+tag+' уншигдсангүй; хадгалав. "));Clear('+coll+')')
UNION=(I2+'// r5.1: H + one-time merge of old sources by SyncKey (unreadable sources are skipped, kept and never overwritten)'
 +I2+'ClearCollect(colCountMarkV22,{Done:false,At:Now()});Clear(colCountMarkV22);'
 'If('+LOADTRY('colCountMarkV22','"C22M" & '+OID)+',Set(varCountMigrateMarkV22,!IsEmpty(colCountMarkV22) && First(colCountMarkV22).Done=true),'
 'Set(varCountMigrateMarkV22,true);Set(varCountHistDiskErrorV22,varCountHistDiskErrorV22 & "C22M уншигдсангүй; хуучин кэшийг дахин нэгтгэсэнгүй. "));Clear(colCountMarkV22);'
 +I2+'ClearCollect(colCountAllV22,AddColumns(colOfflineInventory,SrcRank,100));'
 +SRC('colCountHistDiskV22','varCountHistKeyV22','20','C22H','')+';'
 +I2+'If(!varCountMigrateMarkV22,'
 'ForAll(Filter(colCountSlotOkV22,Slot="R5" && varCountSlotMainV22<>"R5") As o,Collect(colCountAllV22,AddColumns('+PARSE('o.Payload')+',SrcRank,30)));'
 'If(!IsEmpty(Filter(colCountSlotOkV22,Slot="R5")),Set(varCountR5StateV22,"ok")));'
 +I2+'If(!varCountMigrateMarkV22,'+SRC('colCountLegacyDiskV22','varCountLegacyKeyV22','10','C21','varCountLegacyStateV22')+I2+');'
 +I2+'Set(varCountMigrateV22,!varCountMigrateMarkV22 && (varCountLegacyStateV22="ok" || varCountR5StateV22="ok"));'
 +I2+'Set(varCountForeignRowsV22,CountRows(Filter(colCountAllV22,OwnerEmail<>varCountOwner)));'
 +I2+'ClearCollect(colCountAll2V22,AddColumns(Filter(colCountAllV22,OwnerEmail=varCountOwner),SyncedN,If(Synced,1,0),RevN,Coalesce(Revision,0)));Clear(colCountAllV22);'
 +I2+'Set(varCountMigrateConflictV22,CountRows(Filter(ForAll(GroupBy(colCountAll2V22,SyncKey,G) As g,'
 '{n:CountRows(Distinct(Filter(g.G,RevN=Max(g.G,RevN)),'+CSIG('')+'))}),n>1)));'
 +I2+'ClearCollect(colCountWinV22,ForAll(GroupBy(colCountAll2V22,SyncKey,G) As g,'
 'Patch(First(SortByColumns(g.G,"RevN",SortOrder.Descending,"SyncedN",SortOrder.Descending,"SrcRank",SortOrder.Descending)),{SyncKey:g.SyncKey})));'
 +I2+'Set(varCountRewriteV22,!IsEmpty(Filter(colCountWinV22,!Synced && SrcRank<100)) || CountRows(Filter(colCountWinV22,!Synced))<>CountRows(Filter(colOfflineInventory,!Synced)));'
 +I2+'ClearCollect(colOfflineInventory,DropColumns(colCountWinV22,SrcRank,SyncedN,RevN));Clear(colCountAll2V22);Clear(colCountWinV22);'
 +I2+'Set(varCountCoverageFromV22,If(varCountHistNV22 in [1000,400,100] && !IsBlank(varCountHistMinV22),Max('+WIN+',varCountHistMinV22),'+WIN+'));'
 +I2+'Set(varCountIntegrityBlockV22,varCountForeignRowsV22>0 || varCountMigrateConflictV22>0 || varCountSlotSplitV22);'
 +I2+'If(varCountIntegrityBlockV22,Set(varCountDiskSafeV21,false);Set(varCountCacheReady,false);Set(varCountStorageError,"Төхөөрөмжийн кэшид "'
 ' & If(varCountForeignRowsV22>0,"өөр хэрэглэгчийн " & varCountForeignRowsV22 & " мөр ","") & If(varCountMigrateConflictV22>0,varCountMigrateConflictV22 & " зөрчилтэй мөр ","")'
 ' & If(varCountSlotSplitV22,"ижил дугаартай зөрүүтэй хуулбар ","") & "илэрлээ. Файлуудыг хадгалж, хадгалалт/илгээлтийг зогсоов. IT-д хандана уу."));'
 +I2+'RemoveIf(colOfflineInventory,Synced && !IsBlank(CountDate) && CountDate<'+WIN+')\n')
GUARD=('\n      // r5.1: unusable P files -> unsafe (nothing is overwritten)\n'
 '      If(varCountSlotBlockV22,Set(varCountDiskSafeV21,false);Set(varCountLoadErrorV21,true);'
 'Set(varCountStorageError,"Төхөөрөмжийн тооллогын файлыг найдвартай уншиж чадсангүй. Хуучин файлыг дарж бичихгүй."));')
s=rep(s,'\n      If(varCountDiskSafeV21,\n       // v3.6.8: set-based merge',GUARD+'\n      If(varCountDiskSafeV21,'+UNION+'      );\n      If(varCountDiskSafeV21,\n       // v3.6.8: set-based merge')
# legacy V19 cache: merged only before the migration marker exists
s=rep(s,'ClearCollect(colPrevAddV368,Filter(colPreviousCountV21,OwnerEmail=varCountOwner && !(SyncKey in colOfflineInventory.SyncKey)));',
        'ClearCollect(colPrevAddV368,Filter(colPreviousCountV21,!varCountMigrateMarkV22 && OwnerEmail=varCountOwner && !(SyncKey in colOfflineInventory.SyncKey)));')
s=rep(s,'If(varPerfPrevCandidatesV368=0 && !IsEmpty(colCountDiskV21),Set(varCountCacheReady,true)',
        'If(varPerfPrevCandidatesV368=0 && !IsEmpty(colCountDiskV21) && !varCountMigrateV22 && !varCountRewriteV22 && !'+BLOCK+',Set(varCountCacheReady,true)')
# 4c. migration: separate steps, each with its own result
VKEY='v.SyncKey=p.SyncKey && '+VSIG('v.')+'='+VSIG('p.')
def READ(key): return ('ClearCollect(colCountVerifyV22,{Schema:22,Owner:"",Payload:"[]",Seq:0});Clear(colCountVerifyV22);LoadData(colCountVerifyV22,'+key+',true);'
                      'ClearCollect(colCountVerifyRowsV22,'+PARSE('First(colCountVerifyV22).Payload')+')')
NSYNC='CountRows(Filter(colOfflineInventory,Synced))'
KEEP1='Mid(varCountSlotKeepV22,2,1)'
FIN=('      RemoveIf(colOfflineInventory,Synced && !IsBlank(CountDate) && CountDate<'+WIN+');\n'
 '      // r5.1: old files are retired only after P and H were written, read back and matched row by row (each step checked separately)\n'
 '      If(varCountMigrateV22 && varCountDiskSafeV21 && varCountCacheReady && !'+BLOCK+' && !varCountHistLockV22,\n'
 '       Set(varCountMigP22,IfError('+PWRITE+';varCountW2V22,false));\n'
 '       Set(varCountMigH22,varCountMigP22 && IfError('+HWRITE+';true,false));\n'
 '       Set(varCountMigVP22,varCountMigH22 && IfError('+READ('"C22P" & '+KEEP1+' & '+OID)+';\n'
 '        ClearCollect(colCountVerifyPendV22,Filter(colOfflineInventory,!Synced));\n'
 '        CountRows(colCountVerifyV22)=1 && First(colCountVerifyV22).Schema=22 && First(colCountVerifyV22).Owner=varCountOwner && '
 'First(colCountVerifyV22).Seq=varCountSeqV22 && CountIf(colCountVerifyRowsV22,'+ROWERR+')=0 && CountIf(colCountVerifyRowsV22,Synced)=0 && CountRows(colCountVerifyRowsV22)=CountRows(colCountVerifyPendV22) && '
 'CountRows(Distinct(colCountVerifyRowsV22,SyncKey))=CountRows(colCountVerifyRowsV22) && '
 'CountRows(Filter(colCountVerifyPendV22 As p,IsBlank(LookUp(colCountVerifyRowsV22 As v,'+VKEY+').SyncKey)))=0,false));\n'
 '       Set(varCountMigVH22,varCountMigVP22 && IfError('+READ('varCountHistKeyV22')+';\n'
 '        CountRows(colCountVerifyV22)=1 && First(colCountVerifyV22).Schema=22 && First(colCountVerifyV22).Owner=varCountOwner && '
 'CountIf(colCountVerifyRowsV22,'+ROWERR+')=0 && CountIf(colCountVerifyRowsV22,!Synced)=0 && '
 'CountRows(colCountVerifyRowsV22) in [Min(1000,'+NSYNC+'),Min(400,'+NSYNC+'),Min(100,'+NSYNC+')] && '
 'CountRows(Distinct(colCountVerifyRowsV22,SyncKey))=CountRows(colCountVerifyRowsV22) && '
 'CountRows(Filter(colCountVerifyRowsV22 As v,IsBlank(LookUp(colOfflineInventory As p,p.Synced && '+VKEY+').SyncKey)))=0 && '
 'CountRows(Filter(FirstN(SortByColumns(Filter(colOfflineInventory,Synced),"CountDate",SortOrder.Descending),CountRows(colCountVerifyRowsV22)) As p,IsBlank(LookUp(colCountVerifyRowsV22 As v,'+VKEY+').SyncKey)))=0,false));\n'
 '       Set(varCountMigrateOkV22,varCountMigVH22);\n'
 '       If(varCountMigrateOkV22 && varCountLegacyStateV22<>"bad" && varCountR5StateV22<>"bad",\n'
 '        ClearCollect(colCountMarkV22,{Done:true,At:Now()});Set(varCountMigrateMarkV22,IfError(SaveData(colCountMarkV22,"C22M" & '+OID+');true,false));Clear(colCountMarkV22));\n'
 '       If(varCountMigrateOkV22 && varCountMigrateMarkV22 && varCountMigrateDeleteV22,\n'
 '        Set(varCountDelC21V22,If(varCountLegacyStateV22="ok",IfError(ClearData(varCountLegacyKeyV22);"deleted","delete failed"),"kept"));\n'
 '        Set(varCountDelR5V22,If(varCountR5StateV22="ok",IfError(ClearData("C22P" & '+OID+');"deleted","delete failed"),"kept"));\n'
 '        Set(varCountMigrateStatusV22,"verified · C21 " & varCountDelC21V22 & " · r5 " & varCountDelR5V22),\n'
 '        varCountMigrateOkV22,Set(varCountMigrateStatusV22,"verified · marker " & If(varCountMigrateMarkV22,"ok","FAILED") & " · delete disabled"),\n'
 '        Set(varCountMigrateStatusV22,"not verified (P " & varCountMigP22 & ", H " & varCountMigH22 & ", P read " & varCountMigVP22 & ", H read " & varCountMigVH22 & ") · old files kept"));\n'
 '       Clear(colCountVerifyV22);Clear(colCountVerifyRowsV22);Clear(colCountVerifyPendV22));\n'
 '      If('+BLOCK+' || varCountSlotBlockV22 || !IsBlank(varCountSlotErrV22) || !IsBlank(varCountHistDiskErrorV22),Notify("Төхөөрөмжийн кэш: " & '
 'If('+BLOCK+' || varCountSlotBlockV22,varCountStorageError & " ","") & If(!IsBlank(varCountSlotErrV22),"уншигдаагүй хуулбар: " & varCountSlotErrV22 & ". ","") & varCountHistDiskErrorV22,'
 'If('+BLOCK+' || varCountSlotBlockV22,NotificationType.Error,NotificationType.Warning)));\n'
 '      Clear(colCountSlotV22);Clear(colCountSlotOkV22);Clear(colCountSlotTmpV22);Clear(colCountSeqStatV22);\n')
s=rep(s,'Clear(colPreviousCountV21);\n      Set(varCountLoadDoneV21,true);','Clear(colPreviousCountV21);\n'+FIN+'      Set(varCountLoadDoneV21,true);')
wr('App.pa.yaml',s)
# ---- 5. upload timers: when the queue is empty, persist H at most every 10 minutes
def prop_span(L,ctl,prop):
    ci=next(i for i,l in enumerate(L) if l.strip()=='- '+ctl+':')
    ind0=len(L[ci])-len(L[ci].lstrip())
    pi=next(i for i in range(ci+1,len(L)) if L[i].strip().startswith(prop+':'))
    assert all((len(L[i])-len(L[i].lstrip())>ind0) for i in range(ci+1,pi+1)),'left control'
    pind=len(L[pi])-len(L[pi].lstrip())
    if L[pi].strip().endswith('|-'):
        j=pi+1
        while j<len(L) and (L[j].strip()=='' or len(L[j])-len(L[j].lstrip())>pind): j+=1
        last=j-1
        while L[last].strip()=='': last-=1
        return pi+1,last
    return pi,pi
def append_prop(fn,ctl,prop,suffix):
    L=rd(fn).split('\n'); first,last=prop_span(L,ctl,prop)
    assert '//' not in L[last],(fn,ctl,'comment on last line')
    L[last]=L[last]+suffix; wr(fn,'\n'.join(L))
def wrap_prop(fn,ctl,prop,prefix):
    L=rd(fn).split('\n'); first,last=prop_span(L,ctl,prop)
    assert '//' not in L[last],(fn,ctl,'comment on last line')
    k=L[first].index('='); L[first]=L[first][:k]+'='+prefix+L[first][k+1:]; L[last]=L[last]+')'; wr(fn,'\n'.join(L))
TSUF=(';If((IsBlank(varCountHistDiskAtV22) || varCountHistDiskAtV22<DateAdd(Now(),-10,TimeUnit.Minutes)) && '
      'varCountDiskSafeV21 && varCountCacheReady && IsEmpty(Filter(colOfflineInventory,!Synced)),'
      'IfError('+HWRITE+',Set(varCountHistDiskErrorV22,FirstError.Message)))')
for fn,ctl in [('ScrCountHome.pa.yaml','uploadQueueV16_10'),('нүүр.pa.yaml','uploadQueueV16_11'),('ScrHistory.pa.yaml','uploadQueueV16_12')]:
    append_prop(fn,ctl,'OnTimerEnd',TSUF)
# ---- 6. integrity block in front of every SharePoint write path
BMSG='Notify("Төхөөрөмжийн тооллогын кэшид зөрчил илэрсэн тул SharePoint руу бичихгүй. IT-д хандана уу.",NotificationType.Error)'
GUARDED=[('ScrCountHome.pa.yaml','countHomeButton5','OnSelect',BMSG),('ScrCountHome.pa.yaml','uploadQueueV16_10','OnTimerEnd','false'),
         ('ScrHistory.pa.yaml','Button16','OnSelect',BMSG),('ScrHistory.pa.yaml','Button17','OnSelect',BMSG),
         ('ScrHistory.pa.yaml','hDeleteConfirmV16','OnSelect',BMSG),('ScrHistory.pa.yaml','uploadQueueV16_12','OnTimerEnd','false'),
         ('scrWarehouses.pa.yaml','Button1_2','OnSelect',BMSG),('нүүр.pa.yaml','Button5','OnSelect',BMSG),('нүүр.pa.yaml','uploadQueueV16_11','OnTimerEnd','false')]
for fn,ctl,prop,act in GUARDED: wrap_prop(fn,ctl,prop,'If('+BLOCK+','+act+',')
# every property that can Patch(InventoryCount) must be guarded
for f in FILES:
    for k,v in props(rd(f)).items():
        if 'Patch(InventoryCount' in v: assert v.startswith('=If('+BLOCK+','),(f,k)
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
