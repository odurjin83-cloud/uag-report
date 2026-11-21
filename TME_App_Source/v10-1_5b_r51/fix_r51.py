# r4.2 Version 3 (tested build) -> r5.1 : device count store that cannot lose an acknowledged count
#  P  unsent rows, TWO alternating slots "C22PA"/"C22PB" + Seq. A write goes to the slot that does NOT hold the
#     newest valid copy; Seq advances only after SaveData succeeded. Load picks the newest valid slot, so a crash
#     during a write falls back to the previous complete copy. A slot that exists but cannot be LOADED blocks saving
#     (never overwrite what we could not read).
#  H  sent rows, newest 1,000 -> 400 -> 100 -> 0 (Power Fx JSON() output limit); history only, never unsent rows.
#  C21 (old full-history file) is merged by SyncKey on every start while it exists (first migration and crash
#     mid-migration). The newer P always wins; a same-SyncKey row with different item/location/qty/date is a
#     conflict: nothing is overwritten and C21 is kept. C21 (and the r5 test file "C22P") is removed only after
#     P and H were read back and matched by SyncKey+ItemNo+LocationCode+CountQty+CountDate.
#  Unsent rows: warning from 800, new counts blocked from 1,200 until synced (keeps P far below the JSON limit).
#  Memory: unsent rows + sent rows of today+2 days. SharePoint restore: same window.
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
WIN='DateAdd(Today(),-Coalesce(varCountWindowDaysV22,2),TimeUnit.Days)'
UNSENT='CountRows(Filter(colOfflineInventory,OwnerEmail=varCountOwner && !Synced))'
BADP='Error({Kind:ErrorKind.Validation,Message:"Тооллогын кэшийг бэлдэж чадсангүй. Хуучин файлыг дарж бичсэнгүй."})'
BADW='Error({Kind:ErrorKind.Validation,Message:"Төхөөрөмжид бичиж чадсангүй."})'
SLOTKEY='"C22P" & If(Mod(_seq,2)=0,"A","B") & '+OID
# P write (every save/upload): validated payload -> other slot -> Seq advances only after a successful SaveData
PWRITE=('With({_p22:JSON(Filter(colOfflineInventory,!Synced),JSONFormat.Compact),_seq:Coalesce(varCountSeqV22,0)+1},'
        'If(IsError(_p22) || Left(_p22,1)<>"[" || Right(_p22,1)<>"]",'+BADP+','
        'ClearCollect(colCountDiskV21,{Schema:22,Owner:varCountOwner,Payload:_p22,Seq:_seq});'
        'If(IsError(SaveData(colCountDiskV21,'+SLOTKEY+')),'+BADW+',Set(varCountSeqV22,_seq))))')
HSEL='FirstN(SortByColumns(Filter(colOfflineInventory,Synced),"CountDate",SortOrder.Descending),{n})'
HJSON=('IfError(JSON('+HSEL.format(n=1000)+',JSONFormat.Compact),IfError(JSON('+HSEL.format(n=400)+',JSONFormat.Compact),'
       'IfError(JSON('+HSEL.format(n=100)+',JSONFormat.Compact),"[]")))')
HWRITE=('With({_h22:'+HJSON+'},If(IsError(_h22) || Left(_h22,1)<>"[" || Right(_h22,1)<>"]",'+BADP+','
        'ClearCollect(colCountHistDiskV22,{Schema:22,Owner:varCountOwner,Payload:_h22});'
        'If(IsError(SaveData(colCountHistDiskV22,"C22H" & '+OID+')),'+BADW+',Set(varCountHistDiskAtV22,Now()))))')
# ---- 1. all 16 device writes: unsent rows only, two slots
tot=0
for f in FILES:
    t=rd(f)
    t,c=re.subn(r'ClearCollect\(colCountDiskV21,\{Schema:21,Owner:varCountOwner,Payload:JSON\(colOfflineInventory,JSONFormat\.Compact\)\}\);\s*SaveData\(colCountDiskV21,varCountCacheKey\)',
                lambda m:PWRITE,t)
    if c: tot+=c; wr(f,t)
assert tot==16,tot
# ---- 2. SharePoint restore: window only; after merge prune + persist H (own IfError, never blocks P)
glob("Filter(InventoryCount,Counter=varCountOwner || (Counter=User().FullName && 'Created By'.Email=varCountOwner))",
     "Filter(InventoryCount,(Counter=varCountOwner || (Counter=User().FullName && 'Created By'.Email=varCountOwner)) && Created>="+WIN+")",6)
glob('ClearCollect(colOfflineInventory,DropColumns(colHistoryMergedV16,MergePriority));',
     'ClearCollect(colOfflineInventory,DropColumns(colHistoryMergedV16,MergePriority));'
     'RemoveIf(colOfflineInventory,Synced && !IsBlank(CountDate) && CountDate<'+WIN+');'
     'If(varCountDiskSafeV21,IfError('+HWRITE+',Set(varCountHistDiskErrorV22,FirstError.Message)));',6)
# ---- 3. save button: unsent-row limits
s=rd('scrWarehouses.pa.yaml')
s=rep(s,'IsBlank(varCountOwner) || varCountOwner<>Lower(Trim(User().Email)),Notify("Microsoft 365 хэрэглэгчийг шалгана уу.",NotificationType.Error),',
 'IsBlank(varCountOwner) || varCountOwner<>Lower(Trim(User().Email)),Notify("Microsoft 365 хэрэглэгчийг шалгана уу.",NotificationType.Error),'
 +UNSENT+'>=1200,Notify("Илгээгээгүй 1,200 тооллого хуримтлагдсан. Өгөгдөл алдагдахаас сэргийлж шинэ тооллогыг түр хаалаа. Сүлжээнд холбогдож илгээнэ үү.",NotificationType.Error,10000),')
s=rep(s,'Set(varCountLastSavedAtV21,Now());Set(varCountLastSavedQtyV21,_qty);',
 'Set(varCountLastSavedAtV21,Now());Set(varCountLastSavedQtyV21,_qty);'
 'If('+UNSENT+'>=800,Notify("Илгээгээгүй " & '+UNSENT+' & " тооллого байна. 1,200 хүрэхэд шинэ тооллого хаагдана. Сүлжээнд холбогдож илгээнэ үү.",NotificationType.Warning,4000));')
wr('scrWarehouses.pa.yaml',s)
# ---- 4. App.OnStart
s=rd('App.pa.yaml')
s=rep(s,'Set(varCountCacheKey,"C21" & '+OID+');',
 'Set(varCountCacheKey,"C22P" & '+OID+');Set(varCountHistKeyV22,"C22H" & '+OID+');Set(varCountLegacyKeyV22,"C21" & '+OID+');'
 'Set(varCountMigrateV22,false);Set(varCountWindowDaysV22,2);Set(varCountHistDiskErrorV22,"");Set(varCountSeqV22,0);Set(varCountSlotErrV22,"");'
 'Set(varCountMigrateConflictV22,0);Set(varCountMigrateOkV22,false);'
 'ClearCollect(colCountHistDiskV22,{Schema:22,Owner:"",Payload:"[]"});Clear(colCountHistDiskV22);')
s=rep(s,'ClearCollect(colCountDiskV21,{Schema:21,Owner:"",Payload:"[]"});Clear(colCountDiskV21);',
        'ClearCollect(colCountDiskV21,{Schema:21,Owner:"",Payload:"[]",Seq:0});Clear(colCountDiskV21);')
# 4a. load: newest valid slot (A, B, or the r5 test file); an unloadable slot makes the store unsafe
m=re.search(r'\n(\s*)LoadData\(colCountDiskV21,varCountCacheKey,true\);\n',s); assert m; ind=m.group(1)
def slot(key,tag):
    return (ind+'Clear(colCountSlotTmpV22);IfError(LoadData(colCountSlotTmpV22,'+key+',true);'
            'Collect(colCountSlotV22,AddColumns(colCountSlotTmpV22,Slot,"'+tag+'")),Set(varCountSlotErrV22,varCountSlotErrV22 & "'+tag+'"));\n')
LOAD=('\n'+ind+'ClearCollect(colCountSlotTmpV22,{Schema:21,Owner:"",Payload:"[]",Seq:0});Clear(colCountSlotTmpV22);'
      'ClearCollect(colCountSlotV22,AddColumns(colCountSlotTmpV22,Slot,""));Clear(colCountSlotV22);\n'
      +slot('"C22PA" & '+OID,'A')+slot('"C22PB" & '+OID,'B')+slot('"C22P" & '+OID,'R5')+
      ind+'If(!IsBlank(varCountSlotErrV22),Error({Kind:ErrorKind.Validation,Message:"Төхөөрөмжийн тооллогын файлыг уншиж чадсангүй (" & varCountSlotErrV22 & "). Дарж бичихгүй."}));\n'
      +ind+'ClearCollect(colCountSlotOkV22,FirstN(SortByColumns(Filter(colCountSlotV22,Schema=22 && Owner=varCountOwner && Left(Payload,1)="[" && Right(Payload,1)="]" && !IsError(ParseJSON(Payload))),"Seq",SortOrder.Descending),1));\n'
      +ind+'ClearCollect(colCountDiskV21,ShowColumns(colCountSlotOkV22,Schema,Owner,Payload,Seq));\n'
      +ind+'Set(varCountSeqV22,Coalesce(First(colCountSlotOkV22).Seq,0));Set(varCountMigrateV22,First(colCountSlotOkV22).Slot="R5" || CountRows(Filter(colCountSlotV22,Slot="R5"))>0);\n'
      +ind+'Clear(colCountSlotV22);Clear(colCountSlotTmpV22);Clear(colCountSlotOkV22);\n')
s=s[:m.start()]+LOAD+s[m.end():]
s=rep(s,'If(First(colCountDiskV21).Schema<>21 || First(colCountDiskV21).Owner<>varCountOwner,',
        'If(First(colCountDiskV21).Schema<>22 || First(colCountDiskV21).Owner<>varCountOwner,')
mm=re.search(r'ClearCollect\(colOfflineInventory,ForAll\(Table\(ParseJSON\(First\(colCountDiskV21\)\.Payload\)\) As r,(\{.*?Synced:Boolean\(r\.Value\.Synced\)\})\)\)',s,re.S)
assert mm; MAP=mm.group(1)
# 4b. after a safe load: merge C21 by SyncKey (P wins; conflicts keep C21), then H, then prune to the window
I2='\n       '
LEG=(I2+'ClearCollect(colCountLegacyDiskV22,{Schema:21,Owner:"",Payload:"[]"});Clear(colCountLegacyDiskV22);'
 'IfError(LoadData(colCountLegacyDiskV22,varCountLegacyKeyV22,true);'
 'If(!IsEmpty(colCountLegacyDiskV22),'
 'If(CountRows(colCountLegacyDiskV22)<>1 || First(colCountLegacyDiskV22).Schema<>21 || First(colCountLegacyDiskV22).Owner<>varCountOwner,'
 'Set(varCountHistDiskErrorV22,"Хуучин C21 кэшийн бүтэц таарахгүй тул шилжүүлээгүй, устгаагүй."),'
 'ClearCollect(colCountLegacyRowsV22,ForAll(Table(ParseJSON(First(colCountLegacyDiskV22).Payload)) As r,'+MAP+'));'
 'If(CountIf(colCountLegacyRowsV22,IsError(SyncKey) || IsBlank(SyncKey) || IsError(Synced) || IsError(OwnerEmail) || IsError(CountQty) || IsError(CountDate))>0,'
 'Set(varCountHistDiskErrorV22,"Хуучин C21 кэшийн мөр уншигдсангүй тул шилжүүлээгүй, устгаагүй."),'
 'Set(varCountMigrateConflictV22,CountRows(Filter(colCountLegacyRowsV22 As l,l.OwnerEmail=varCountOwner && !IsBlank(LookUp(colOfflineInventory As p,p.SyncKey=l.SyncKey).SyncKey) && '
 'IsBlank(LookUp(colOfflineInventory As p,p.SyncKey=l.SyncKey && p.ItemNo=l.ItemNo && p.LocationCode=l.LocationCode && p.CountQty=l.CountQty).SyncKey))));'
 'ClearCollect(colCountLegacyAddV22,ForAll(GroupBy(Filter(colCountLegacyRowsV22,OwnerEmail=varCountOwner && !(SyncKey in colOfflineInventory.SyncKey)),SyncKey,LegRows) As g,'
 'Patch(First(SortByColumns(g.LegRows,"Revision",SortOrder.Descending)),{SyncKey:g.SyncKey})));'
 'Collect(colOfflineInventory,colCountLegacyAddV22);Set(varCountMigrateV22,true));'
 'Clear(colCountLegacyRowsV22);Clear(colCountLegacyAddV22)));Clear(colCountLegacyDiskV22),'
 'Clear(colCountLegacyDiskV22);Clear(colCountLegacyRowsV22);Set(varCountHistDiskErrorV22,"Хуучин C21 кэшийг уншиж чадсангүй; устгаагүй. " & FirstError.Message));')
HLOAD=(LEG+I2+'If(!varCountMigrateV22,IfError(LoadData(colCountHistDiskV22,varCountHistKeyV22,true);'
 'If(!IsEmpty(colCountHistDiskV22) && First(colCountHistDiskV22).Schema=22 && First(colCountHistDiskV22).Owner=varCountOwner,'
 'ClearCollect(colCountHistRowsV22,ForAll(Table(ParseJSON(First(colCountHistDiskV22).Payload)) As r,'+MAP+'));'
 'ClearCollect(colCountHistAddV22,Filter(colCountHistRowsV22,!IsError(SyncKey) && !IsBlank(SyncKey) && !(SyncKey in colOfflineInventory.SyncKey)));'
 'Collect(colOfflineInventory,colCountHistAddV22);Clear(colCountHistRowsV22);Clear(colCountHistAddV22));Clear(colCountHistDiskV22),'
 'Clear(colCountHistDiskV22);Clear(colCountHistRowsV22);Set(varCountHistDiskErrorV22,FirstError.Message)));'
 +I2+'RemoveIf(colOfflineInventory,Synced && !IsBlank(CountDate) && CountDate<'+WIN+')\n')
GUARD=('\n      // r5.1: a slot that could not be loaded makes the store unsafe, whatever happened inside the chain above\n'
 '      If(!IsBlank(varCountSlotErrV22),Set(varCountDiskSafeV21,false);Set(varCountLoadErrorV21,true);'
 'Set(varCountStorageError,"Төхөөрөмжийн тооллогын файлыг уншиж чадсангүй. Хуучин файлыг дарж бичихгүй."));')
s=rep(s,'\n      If(varCountDiskSafeV21,\n       // v3.6.8: set-based merge',GUARD+'\n      If(varCountDiskSafeV21,'+HLOAD+'      );\n      If(varCountDiskSafeV21,\n       // v3.6.8: set-based merge')
s=rep(s,'If(varPerfPrevCandidatesV368=0 && !IsEmpty(colCountDiskV21),Set(varCountCacheReady,true)',
        'If(varPerfPrevCandidatesV368=0 && !IsEmpty(colCountDiskV21) && !varCountMigrateV22,Set(varCountCacheReady,true)')
# 4c. finalize migration: H write, read back P (slot of varCountSeqV22) and H, match by key fields, then remove C21 / r5 file
VKEY='v.SyncKey=p.SyncKey && v.ItemNo=p.ItemNo && v.LocationCode=p.LocationCode && v.CountQty=p.CountQty && Text(v.CountDate,"yyyymmddhhmmss")=Text(p.CountDate,"yyyymmddhhmmss")'
READ=lambda key:('ClearCollect(colCountVerifyV22,{Schema:22,Owner:"",Payload:"[]",Seq:0});Clear(colCountVerifyV22);LoadData(colCountVerifyV22,'+key+',true);'
                 'ClearCollect(colCountVerifyRowsV22,ForAll(Table(ParseJSON(First(colCountVerifyV22).Payload)) As r,'+MAP+'));')
FIN=('      // r5.1: migration is finished only after P and H were read back and matched row by row\n'
 '      If(varCountMigrateV22 && varCountDiskSafeV21 && varCountCacheReady && varCountMigrateConflictV22=0,\n'
 '       IfError('+HWRITE+',Set(varCountHistDiskErrorV22,FirstError.Message));\n'
 '       Set(varCountMigrateOkV22,false);\n'
 '       IfError(\n'
 '        With({_seq:varCountSeqV22},'+READ(SLOTKEY)[:-1]+')\n'
 '        ;ClearCollect(colCountVerifyPendV22,Filter(colOfflineInventory,!Synced));\n'
 '        Set(varCountMigrateOkV22,CountRows(colCountVerifyV22)=1 && First(colCountVerifyV22).Schema=22 && First(colCountVerifyV22).Owner=varCountOwner && '
 'First(colCountVerifyV22).Seq=varCountSeqV22 && CountRows(colCountVerifyRowsV22)=CountRows(colCountVerifyPendV22) && '
 'CountRows(Distinct(colCountVerifyRowsV22,SyncKey))=CountRows(colCountVerifyRowsV22) && '
 'CountRows(Filter(colCountVerifyPendV22 As p,IsBlank(LookUp(colCountVerifyRowsV22 As v,'+VKEY+').SyncKey)))=0);\n'
 '        '+READ('varCountHistKeyV22')+'\n'
 '        Set(varCountMigrateOkV22,varCountMigrateOkV22 && CountRows(colCountVerifyV22)=1 && First(colCountVerifyV22).Schema=22 && First(colCountVerifyV22).Owner=varCountOwner && '
 'CountRows(colCountVerifyRowsV22) in [Min(1000,CountRows(Filter(colOfflineInventory,Synced))),Min(400,CountRows(Filter(colOfflineInventory,Synced))),Min(100,CountRows(Filter(colOfflineInventory,Synced))),0] && '
 'CountRows(Distinct(colCountVerifyRowsV22,SyncKey))=CountRows(colCountVerifyRowsV22) && '
 'CountRows(Filter(colCountVerifyRowsV22 As v,IsBlank(LookUp(colOfflineInventory As p,p.Synced && '+VKEY+').SyncKey)))=0);\n'
 '        true,Set(varCountMigrateOkV22,false));\n'
 '       If(varCountMigrateOkV22,IfError(ClearData(varCountLegacyKeyV22);ClearData("C22P" & '+OID+');Set(varCountMigrateV22,false),Set(varCountHistDiskErrorV22,FirstError.Message)),\n'
 '        Set(varCountHistDiskErrorV22,"Шилжүүлэлтийг баталгаажуулж чадсангүй. Хуучин файлыг үлдээв."));\n'
 '       Clear(colCountVerifyV22);Clear(colCountVerifyRowsV22);Clear(colCountVerifyPendV22));\n'
 '      If(varCountMigrateConflictV22>0,Notify("Хуучин кэшид " & varCountMigrateConflictV22 & " тооллого шинэ кэшээс өөр утгатай байна. Аль нь ч дарагдаагүй; IT-д мэдэгдэнэ үү.",NotificationType.Warning));\n')
s=rep(s,'Clear(colPreviousCountV21);\n      Set(varCountLoadDoneV21,true);',
 'Clear(colPreviousCountV21);\n'
 '      RemoveIf(colOfflineInventory,Synced && !IsBlank(CountDate) && CountDate<'+WIN+');\n'+FIN+
 '      Set(varCountLoadDoneV21,true);')
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
            assert bal(b[key])==(0,0),(key,bal(b[key])); n+=1
            ctl,prop=key.rsplit('.',1)
            open(f'{OUT}{n:02d}_{fn[:-8]}_{ctl}_{prop}.txt','w',encoding='utf-8').write(b[key][1:]); print(n,key,len(b[key]))
allsrc=''.join(rd(f) for f in FILES)
print('full-table JSON:',allsrc.count('JSON(colOfflineInventory,'),'| old key writes:',allsrc.count('SaveData(colCountDiskV21,varCountCacheKey)'))
