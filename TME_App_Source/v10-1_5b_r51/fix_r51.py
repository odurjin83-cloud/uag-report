# r4.2 Version 3 (tested build) -> r5.1 (rev 2, after OpenClaw + Copilot static review of rev 1)
# Goal: a count shown as saved is never lost; nothing unreadable is ever overwritten; nothing is deleted before it was proven copied.
#  P  unsent rows only, THREE rotating slots "C22PA/B/C" + Seq. A write goes to the oldest slot that is neither the newest
#     copy nor marked bad; Seq/newest advance only after SaveData succeeded; a failed write marks that slot bad.
#     No writable slot -> write refused (old copies kept).
#  LOAD every source is read (LoadData retried once): P slots A/B/C, r5 test file "C22P", history "C22H", old "C21".
#     A source that cannot be loaded or parsed is skipped and never overwritten/deleted. Saving is blocked only when
#     P slots exist but none is valid. All readable rows are merged by SyncKey: highest Revision wins, then Synced, then
#     newest source. Same SyncKey + same Revision + different (item, location, qty, date, owner) = conflict -> warned,
#     sources kept. Rows of another owner -> warned, sources kept, saving blocked.
#  H  sent rows, newest 1000 -> 400 -> 100; if even 100 fails H is not written (old H kept). Never contains unsent rows.
#  Migration cleanup (C21 + r5 "C22P") only after P and H were written, read back and matched by SyncKey + signature,
#     AND only when varCountMigrateDeleteV22=true (App.OnStart; TEST default false).
#  Unsent rows (all owners): warning from 800, new counts blocked from 1,200 (only Button1_2 creates rows).
#  Memory: unsent rows + sent rows since the window start (today-2 days, or varCountWindowStartV22 for a commission).
# run from repo root: python3 TME_App_Source/v10-1_5b_r51/fix_r51.py <dir with props.py>
import os,sys,re
sys.path.insert(0,sys.argv[1]); from props import props
BASE='TME_App_Source/v10-1_5b_r42count_studio/Src/'
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
def SIG(p): return p+'ItemNo & "|" & '+p+'LocationCode & "|" & Text('+p+'CountQty) & "|" & Text('+p+'CountDate,"yyyymmddhhmmss") & "|" & '+p+'OwnerEmail'
def ERR(msg): return 'Error({Kind:ErrorKind.Validation,Message:"'+msg+'"})'
TARGET='First(SortByColumns(Filter(colCountSlotSeqV22,!Bad && Slot<>Coalesce(varCountSlotNewV22,"")),"Seq",SortOrder.Ascending)).Slot'
PWRITE=('With({_p22:JSON(Filter(colOfflineInventory,!Synced),JSONFormat.Compact),_seq:Coalesce(varCountSeqV22,0)+1,_t:'+TARGET+'},'
 'If(IsError(_p22) || Left(_p22,1)<>"[" || Right(_p22,1)<>"]",'+ERR('Тооллогын кэшийг бэлдэж чадсангүй. Хуучин файлыг дарж бичсэнгүй.')+','
 'CountRows(Filter(colOfflineInventory,!Synced && OwnerEmail<>varCountOwner))>0,'+ERR('Өөр хэрэглэгчийн илгээгээгүй мөр байна. Хадгалалтыг зогсоов; IT-д хандана уу.')+','
 'IsBlank(_t),'+ERR('Төхөөрөмжийн нөөц файлууд бичигдэхгүй байна. Хуучин хуулбарыг хадгалж, шинээр бичсэнгүй.')+','
 'ClearCollect(colCountDiskV21,{Schema:22,Owner:varCountOwner,Payload:_p22,Seq:_seq});'
 'If(IfError(SaveData(colCountDiskV21,"C22P" & _t & '+OID+');true,false),'
 'Set(varCountSeqV22,_seq);Patch(colCountSlotSeqV22,LookUp(colCountSlotSeqV22,Slot=_t),{Seq:_seq});Set(varCountSlotNewV22,_t),'
 'Patch(colCountSlotSeqV22,LookUp(colCountSlotSeqV22,Slot=_t),{Bad:true});'+ERR('Төхөөрөмжид бичиж чадсангүй.')+')))')
HSEL='FirstN(SortByColumns(Filter(colOfflineInventory,Synced),"CountDate",SortOrder.Descending),{n})'
HJSON=('If(IsEmpty(Filter(colOfflineInventory,Synced)),"[]",IfError(JSON('+HSEL.format(n=1000)+',JSONFormat.Compact),'
       'IfError(JSON('+HSEL.format(n=400)+',JSONFormat.Compact),JSON('+HSEL.format(n=100)+',JSONFormat.Compact))))')
HWRITE=('With({_h22:'+HJSON+'},If(IsError(_h22) || Left(_h22,1)<>"[" || Right(_h22,1)<>"]",'+ERR('Түүхийн кэшийг бэлдэж чадсангүй. Хуучин түүхийг үлдээв.')+','
        'ClearCollect(colCountHistDiskV22,{Schema:22,Owner:varCountOwner,Payload:_h22});'
        'If(IfError(SaveData(colCountHistDiskV22,"C22H" & '+OID+');true,false),Set(varCountHistDiskAtV22,Now()),'+ERR('Түүхийг төхөөрөмжид бичиж чадсангүй.')+')))')
# ---- 1. all 16 device writes
tot=0
for f in FILES:
    t=rd(f)
    t,c=re.subn(r'ClearCollect\(colCountDiskV21,\{Schema:21,Owner:varCountOwner,Payload:JSON\(colOfflineInventory,JSONFormat\.Compact\)\}\);\s*SaveData\(colCountDiskV21,varCountCacheKey\)',lambda m:PWRITE,t)
    if c: tot+=c; wr(f,t)
assert tot==16,tot
# ---- 2. SharePoint restore: window only; after merge prune + persist H (own IfError, never blocks P)
glob("Filter(InventoryCount,Counter=varCountOwner || (Counter=User().FullName && 'Created By'.Email=varCountOwner))",
     "Filter(InventoryCount,(Counter=varCountOwner || (Counter=User().FullName && 'Created By'.Email=varCountOwner)) && Created>="+WIN+")",6)
glob('ClearCollect(colOfflineInventory,DropColumns(colHistoryMergedV16,MergePriority));',
     'ClearCollect(colOfflineInventory,DropColumns(colHistoryMergedV16,MergePriority));'
     'RemoveIf(colOfflineInventory,Synced && !IsBlank(CountDate) && CountDate<'+WIN+');'
     'If(varCountDiskSafeV21,IfError('+HWRITE+',Set(varCountHistDiskErrorV22,FirstError.Message)));',6)
# ---- 3. save button (the only place that creates count rows): unsent-row limits
s=rd('scrWarehouses.pa.yaml')
s=rep(s,'IsBlank(varCountOwner) || varCountOwner<>Lower(Trim(User().Email)),Notify("Microsoft 365 хэрэглэгчийг шалгана уу.",NotificationType.Error),',
 'IsBlank(varCountOwner) || varCountOwner<>Lower(Trim(User().Email)),Notify("Microsoft 365 хэрэглэгчийг шалгана уу.",NotificationType.Error),'
 +UNSENT+'>=1200,Notify("Илгээгээгүй 1,200 тооллого хуримтлагдсан. Өгөгдөл алдагдахаас сэргийлж шинэ тооллогыг түр хаалаа. Сүлжээнд холбогдож илгээнэ үү.",NotificationType.Error,10000),')
s=rep(s,'Set(varCountLastSavedAtV21,Now());Set(varCountLastSavedQtyV21,_qty);',
 'Set(varCountLastSavedAtV21,Now());Set(varCountLastSavedQtyV21,_qty);'
 'If('+UNSENT+'>=800,Notify("Илгээгээгүй " & '+UNSENT+' & " тооллого байна. 1,200 хүрэхэд шинэ тооллого хаагдана. Сүлжээнд холбогдож илгээнэ үү.",NotificationType.Warning,4000));')
# receipt guard: documented IfError form instead of IsError(SaveData(...)) (same as v10-1_5)
s,c=re.subn(r'!IsError\(SaveData\(colCountReceiptDiskV1015,("CountReceiptV1015_" & Substitute\(Text\(User\(\)\.EntraObjectId\),"-",""\))\)\)',lambda m:'IfError(SaveData(colCountReceiptDiskV1015,'+m.group(1)+');true,false)',s); assert c==1,c
wr('scrWarehouses.pa.yaml',s)
# ---- 4. App.OnStart
s=rd('App.pa.yaml')
s=rep(s,'Set(varCountCacheKey,"C21" & '+OID+');',
 'Set(varCountCacheKey,"C22PA" & '+OID+');Set(varCountHistKeyV22,"C22H" & '+OID+');Set(varCountLegacyKeyV22,"C21" & '+OID+');'
 'Set(varCountWindowDaysV22,2);\n'
 '      // r5.1 TEST: old files are verified but NOT deleted. Production: true after the device tests pass.\n'
 '      Set(varCountMigrateDeleteV22,false);'
 'Set(varCountMigrateV22,false);Set(varCountRewriteV22,false);Set(varCountHistDiskErrorV22,"");Set(varCountSeqV22,0);Set(varCountSlotErrV22,"");'
 'Set(varCountSlotNewV22,"");Set(varCountSlotBlockV22,false);Set(varCountMigrateConflictV22,0);Set(varCountForeignRowsV22,0);Set(varCountMigrateOkV22,false);Set(varCountMigrateStatusV22,"");'
 'ClearCollect(colCountHistDiskV22,{Schema:22,Owner:"",Payload:"[]"});Clear(colCountHistDiskV22);'
 'ClearCollect(colCountSlotSeqV22,{Slot:"A",Seq:-1,Bad:false},{Slot:"B",Seq:-1,Bad:false},{Slot:"C",Seq:-1,Bad:false});')
s=rep(s,'ClearCollect(colCountDiskV21,{Schema:21,Owner:"",Payload:"[]"});Clear(colCountDiskV21);',
        'ClearCollect(colCountDiskV21,{Schema:21,Owner:"",Payload:"[]",Seq:0});Clear(colCountDiskV21);')
mm=re.search(r'ClearCollect\(colOfflineInventory,ForAll\(Table\(ParseJSON\(First\(colCountDiskV21\)\.Payload\)\) As r,(\{.*?Synced:Boolean\(r\.Value\.Synced\)\})\)\)',s,re.S)
assert mm; MAP=mm.group(1)
def PARSE(payload): return 'ForAll(Table(ParseJSON('+payload+')) As r,'+MAP+')'
ROWERR='IsError(SyncKey) || IsBlank(SyncKey) || IsError(Synced) || IsError(OwnerEmail) || IsError(CountQty) || IsError(CountDate) || IsError(Revision) || IsError(ItemNo) || IsError(LocationCode)'
# 4a. read every P slot (retry once); pick newest valid as the main payload; mark bad slots; block only if P exists but none is valid
m=re.search(r'\n(\s*)LoadData\(colCountDiskV21,varCountCacheKey,true\);\n',s); assert m; ind=m.group(1)
def LOADTRY(coll,key): return ('If(IfError(LoadData('+coll+','+key+',true);true,false),true,IfError(Clear('+coll+');LoadData('+coll+','+key+',true);true,false))')
def slot(key,tag):
    bad='' if tag=='R5' else ';Patch(colCountSlotSeqV22,LookUp(colCountSlotSeqV22,Slot="'+tag+'"),{Bad:true})'
    return (ind+'Clear(colCountSlotTmpV22);If('+LOADTRY('colCountSlotTmpV22',key)+',Collect(colCountSlotV22,AddColumns(colCountSlotTmpV22,Slot,"'+tag+'")),'
            'Clear(colCountSlotTmpV22);Set(varCountSlotErrV22,varCountSlotErrV22 & "'+tag+' ")'+bad+');\n')
NEWEST='First(SortByColumns(AddColumns(colCountSlotOkV22,SeqN,Coalesce(Seq,0)),"SeqN",SortOrder.Descending))'
LOAD=('\n'+ind+'ClearCollect(colCountSlotTmpV22,{Schema:21,Owner:"",Payload:"[]",Seq:0});Clear(colCountSlotTmpV22);'
      'ClearCollect(colCountSlotV22,AddColumns(colCountSlotTmpV22,Slot,""));Clear(colCountSlotV22);\n'
      +slot('"C22PA" & '+OID,'A')+slot('"C22PB" & '+OID,'B')+slot('"C22PC" & '+OID,'C')+slot('"C22P" & '+OID,'R5')+
      ind+'ClearCollect(colCountSlotOkV22,Filter(colCountSlotV22,Schema=22 && Owner=varCountOwner && Left(Payload,1)="[" && Right(Payload,1)="]" && !IsError(ParseJSON(Payload))));\n'
      +ind+'ForAll(Filter(colCountSlotV22,Slot in ["A","B","C"] && !(Slot in colCountSlotOkV22.Slot)) As b,Patch(colCountSlotSeqV22,LookUp(colCountSlotSeqV22,Slot=b.Slot),{Bad:true}));\n'
      +ind+'ForAll(Filter(colCountSlotOkV22,Slot in ["A","B","C"]) As o,Patch(colCountSlotSeqV22,LookUp(colCountSlotSeqV22,Slot=o.Slot),{Seq:Coalesce(o.Seq,0)}));\n'
      +ind+'Set(varCountSlotBlockV22,IsEmpty(colCountSlotOkV22) && (!IsBlank(varCountSlotErrV22) || !IsEmpty(colCountSlotV22)));\n'
      +ind+'Set(varCountSlotMainV22,'+NEWEST+'.Slot);\n'
      +ind+'ClearCollect(colCountDiskV21,ShowColumns(Filter(colCountSlotOkV22,Slot=varCountSlotMainV22),Schema,Owner,Payload,Seq));\n'
      +ind+'Set(varCountSeqV22,Coalesce(Max(colCountSlotOkV22,Coalesce(Seq,0)),0));\n'
      +ind+'Set(varCountSlotNewV22,First(SortByColumns(AddColumns(Filter(colCountSlotOkV22,Slot in ["A","B","C"]),SeqN,Coalesce(Seq,0)),"SeqN",SortOrder.Descending)).Slot);\n'
      +ind+'If(varCountSlotBlockV22,'+ERR('Төхөөрөмжийн тооллогын файлыг уншиж чадсангүй. Дарж бичихгүй.')+');\n')
s=s[:m.start()]+LOAD+s[m.end():]
s=rep(s,'If(First(colCountDiskV21).Schema<>21 || First(colCountDiskV21).Owner<>varCountOwner,',
        'If(First(colCountDiskV21).Schema<>22 || First(colCountDiskV21).Owner<>varCountOwner,')
# 4b. after a safe load: merge ALL readable sources by SyncKey
I2='\n       '
def SRC(coll,key,rank,tag):
    return (I2+'ClearCollect('+coll+',{Schema:21,Owner:"",Payload:"[]",Seq:0});Clear('+coll+');'
     'If('+LOADTRY(coll,key)+','
     'If(!IsEmpty('+coll+'),If(CountRows('+coll+')<>1 || First('+coll+').Owner<>varCountOwner || IsError(ParseJSON(First('+coll+').Payload)),'
     'Set(varCountHistDiskErrorV22,varCountHistDiskErrorV22 & "'+tag+' бүтэц таарахгүй; хадгалав. "),'
     'ClearCollect(colCountSrcRowsV22,'+PARSE('First('+coll+').Payload')+');'
     'If(CountIf(colCountSrcRowsV22,'+ROWERR+')>0,Set(varCountHistDiskErrorV22,varCountHistDiskErrorV22 & "'+tag+' мөр уншигдсангүй; хадгалав. "),'
     'Collect(colCountAllV22,AddColumns(colCountSrcRowsV22,SrcRank,'+rank+'))'+(';Set(varCountMigrateV22,true)' if tag=='C21' else '')+');Clear(colCountSrcRowsV22))),'
     'Set(varCountHistDiskErrorV22,varCountHistDiskErrorV22 & "'+tag+' уншигдсангүй; хадгалав. "));Clear('+coll+');')
UNION=(I2+'// r5.1: every readable source merged by SyncKey (unreadable sources are skipped and kept)'
 +I2+'ClearCollect(colCountAllV22,AddColumns(colOfflineInventory,SrcRank,100));'
 +I2+'ForAll(Filter(colCountSlotOkV22,Slot<>varCountSlotMainV22) As o,'
 'Collect(colCountAllV22,AddColumns('+PARSE('o.Payload')+',SrcRank,If(o.Slot="R5",30,60))));'
 +I2+'If(!IsEmpty(Filter(colCountSlotOkV22,Slot="R5")),Set(varCountMigrateV22,true));'
 +SRC('colCountHistDiskV22','varCountHistKeyV22','20','C22H')
 +SRC('colCountLegacyDiskV22','varCountLegacyKeyV22','10','C21')
 +I2+'Set(varCountForeignRowsV22,CountRows(Filter(colCountAllV22,OwnerEmail<>varCountOwner)));'
 +I2+'ClearCollect(colCountAllV22,AddColumns(Filter(colCountAllV22,OwnerEmail=varCountOwner),SyncedN,If(Synced,1,0),RevN,Coalesce(Revision,0)));'
 +I2+'Set(varCountMigrateConflictV22,CountRows(Filter(ForAll(GroupBy(colCountAllV22,SyncKey,G) As g,'
 '{n:CountRows(Distinct(Filter(g.G,RevN=Max(g.G,RevN)),'+SIG('')+'))}),n>1)));'
 +I2+'ClearCollect(colCountWinV22,ForAll(GroupBy(colCountAllV22,SyncKey,G) As g,'
 'Patch(First(SortByColumns(g.G,"RevN",SortOrder.Descending,"SyncedN",SortOrder.Descending,"SrcRank",SortOrder.Descending)),{SyncKey:g.SyncKey})));'
 +I2+'Set(varCountRewriteV22,!IsEmpty(Filter(colCountWinV22,!Synced && SrcRank<100)) || CountRows(Filter(colCountWinV22,!Synced))<>CountRows(Filter(colOfflineInventory,!Synced)));'
 +I2+'ClearCollect(colOfflineInventory,DropColumns(colCountWinV22,SrcRank,SyncedN,RevN));'
 +I2+'Clear(colCountAllV22);Clear(colCountWinV22);'
 +I2+'If(varCountForeignRowsV22>0,Set(varCountDiskSafeV21,false);Set(varCountStorageError,"Төхөөрөмжийн кэшид өөр хэрэглэгчийн " & varCountForeignRowsV22 & " мөр байна. Хадгалалтыг зогсоов; IT-д хандана уу."));'
 +I2+'RemoveIf(colOfflineInventory,Synced && !IsBlank(CountDate) && CountDate<'+WIN+')\n')
GUARD=('\n      // r5.1: P slots exist but none is valid -> unsafe (nothing is overwritten)\n'
 '      If(varCountSlotBlockV22,Set(varCountDiskSafeV21,false);Set(varCountLoadErrorV21,true);'
 'Set(varCountStorageError,"Төхөөрөмжийн тооллогын файлыг уншиж чадсангүй. Хуучин файлыг дарж бичихгүй."));')
s=rep(s,'\n      If(varCountDiskSafeV21,\n       // v3.6.8: set-based merge',GUARD+'\n      If(varCountDiskSafeV21,'+UNION+'      );\n      If(varCountDiskSafeV21,\n       // v3.6.8: set-based merge')
s=rep(s,'If(varPerfPrevCandidatesV368=0 && !IsEmpty(colCountDiskV21),Set(varCountCacheReady,true)',
        'If(varPerfPrevCandidatesV368=0 && !IsEmpty(colCountDiskV21) && !varCountMigrateV22 && !varCountRewriteV22,Set(varCountCacheReady,true)')
# 4c. migration cleanup: write P and H explicitly, read both back, match by SyncKey + signature, delete only if enabled
VKEY='v.SyncKey=p.SyncKey && '+SIG('v.')+'='+SIG('p.')
def READ(key): return ('ClearCollect(colCountVerifyV22,{Schema:22,Owner:"",Payload:"[]",Seq:0});Clear(colCountVerifyV22);LoadData(colCountVerifyV22,'+key+',true);'
                      'ClearCollect(colCountVerifyRowsV22,'+PARSE('First(colCountVerifyV22).Payload')+')')
NSYNC='CountRows(Filter(colOfflineInventory,Synced))'
FIN=('      RemoveIf(colOfflineInventory,Synced && !IsBlank(CountDate) && CountDate<'+WIN+');\n'
 '      // r5.1: old files are removed only after P and H were written, read back and matched row by row\n'
 '      If(varCountMigrateV22 && varCountDiskSafeV21 && varCountCacheReady && varCountMigrateConflictV22=0 && varCountForeignRowsV22=0,\n'
 '       Set(varCountMigrateOkV22,false);\n'
 '       IfError(\n'
 '        '+PWRITE+';\n'
 '        '+HWRITE+';\n'
 '        '+READ('"C22P" & varCountSlotNewV22 & '+OID)+';\n'
 '        ClearCollect(colCountVerifyPendV22,Filter(colOfflineInventory,!Synced));\n'
 '        Set(varCountMigrateOkV22,CountRows(colCountVerifyV22)=1 && First(colCountVerifyV22).Schema=22 && First(colCountVerifyV22).Owner=varCountOwner && '
 'First(colCountVerifyV22).Seq=varCountSeqV22 && CountRows(colCountVerifyRowsV22)=CountRows(colCountVerifyPendV22) && '
 'CountRows(Distinct(colCountVerifyRowsV22,SyncKey))=CountRows(colCountVerifyRowsV22) && '
 'CountRows(Filter(colCountVerifyPendV22 As p,IsBlank(LookUp(colCountVerifyRowsV22 As v,'+VKEY+').SyncKey)))=0);\n'
 '        '+READ('varCountHistKeyV22')+';\n'
 '        Set(varCountMigrateOkV22,varCountMigrateOkV22 && CountRows(colCountVerifyV22)=1 && First(colCountVerifyV22).Schema=22 && First(colCountVerifyV22).Owner=varCountOwner && '
 'CountRows(colCountVerifyRowsV22) in [Min(1000,'+NSYNC+'),Min(400,'+NSYNC+'),Min(100,'+NSYNC+')] && '
 'CountRows(Distinct(colCountVerifyRowsV22,SyncKey))=CountRows(colCountVerifyRowsV22) && '
 'CountRows(Filter(colCountVerifyRowsV22 As v,IsBlank(LookUp(colOfflineInventory As p,p.Synced && '+VKEY+').SyncKey)))=0 && '
 'CountRows(Filter(FirstN(SortByColumns(Filter(colOfflineInventory,Synced),"CountDate",SortOrder.Descending),CountRows(colCountVerifyRowsV22)) As p,IsBlank(LookUp(colCountVerifyRowsV22 As v,'+VKEY+').SyncKey)))=0);\n'
 '        true,Set(varCountMigrateOkV22,false));\n'
 '       If(varCountMigrateOkV22 && varCountMigrateDeleteV22,IfError(ClearData(varCountLegacyKeyV22);ClearData("C22P" & '+OID+');Set(varCountMigrateV22,false);Set(varCountMigrateStatusV22,"deleted"),Set(varCountHistDiskErrorV22,FirstError.Message)),\n'
 '        varCountMigrateOkV22,Set(varCountMigrateStatusV22,"verified, delete disabled"),\n'
 '        Set(varCountMigrateStatusV22,"not verified, old files kept"));\n'
 '       Clear(colCountVerifyV22);Clear(colCountVerifyRowsV22);Clear(colCountVerifyPendV22));\n'
 '      If(varCountMigrateConflictV22>0 || !IsBlank(varCountSlotErrV22) || !IsBlank(varCountHistDiskErrorV22),Notify("Төхөөрөмжийн кэш: " & '
 'If(varCountMigrateConflictV22>0,varCountMigrateConflictV22 & " мөр өөр хуулбартай зөрсөн (аль нь ч дарагдаагүй). ","") & '
 'If(!IsBlank(varCountSlotErrV22),"уншигдаагүй хуулбар: " & varCountSlotErrV22 & "(бусдаас сэргээв). ","") & varCountHistDiskErrorV22,NotificationType.Warning));\n'
 '      Clear(colCountSlotV22);Clear(colCountSlotOkV22);Clear(colCountSlotTmpV22);\n')
s=rep(s,'Clear(colPreviousCountV21);\n      Set(varCountLoadDoneV21,true);','Clear(colPreviousCountV21);\n'+FIN+'      Set(varCountLoadDoneV21,true);')
wr('App.pa.yaml',s)
# ---- 5. upload timers: when the queue is empty, persist H at most every 10 minutes
def append_prop(fn,ctl,prop,suffix):
    L=rd(fn).split('\n')
    ci=next(i for i,l in enumerate(L) if l.strip()=='- '+ctl+':')
    ind=len(L[ci])-len(L[ci].lstrip())
    pi=next(i for i in range(ci+1,len(L)) if L[i].strip().startswith(prop+':'))
    assert all((len(L[i])-len(L[i].lstrip())>ind) for i in range(ci+1,pi+1)),'left control'
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
n=0
for fn in FILES:
    a=props(open(BASE+fn,encoding='utf-8').read()); b=props(rd(fn))
    for key in b:
        if a.get(key)!=b[key]:
            assert bal(b[key])==(0,0),(key,bal(b[key]))
            tc=lambda x:len(re.findall(r';\s*\)',re.sub(r'//[^\n]*','',re.sub(r'"[^"]*"','""',x or ''))))
            assert tc(b[key])<=tc(a.get(key)),(key,'new trailing ;')
            n+=1; ctl,prop=key.rsplit('.',1)
            open(f'{OUT}{n:02d}_{fn[:-8]}_{ctl}_{prop}.txt','w',encoding='utf-8').write(b[key][1:]); print(n,key,len(b[key]))
allsrc=''.join(rd(f) for f in FILES)
print('full-table JSON:',allsrc.count('JSON(colOfflineInventory,'),'| old key writes:',allsrc.count('SaveData(colCountDiskV21,varCountCacheKey)'),'| IsError(SaveData:',allsrc.count('IsError(SaveData(colCount'))
