# r4.2 Version 3 (tested build, r42count) or TEST_1 -> r5 (Power Apps MVP-1): device keeps a bounded count history, every save writes only unsent rows.
#  - P file  "C22P"+oid (schema 22): unsent rows only  -> written on every save/upload (was: full history, "C21")
#  - H file  "C22H"+oid (schema 22): sent rows of the last N days -> written only on restore and, throttled, when the queue drains
#  - memory: unsent rows + sent rows of the last N days (N = varCountWindowDaysV22, default 2 -> today + 2 days)
#  - restore from SharePoint: own rows of the window only (was: all own rows, capped at 5000)
#  - one-time migration from "C21": loaded as before, then P and H written, "C21" cleared only after both succeed
#  - H is capped at the newest 1,000 sent rows: Power Fx JSON() fails above 1,048,576 bytes (~1,767 rows measured)
# run from repo root: python3 TME_App_Source/v10-1_5b_r5/fix_r5.py <dir with props.py> [base Src dir]
import os,sys,re
sys.path.insert(0,sys.argv[1]); from props import props
B='TME_App_Source/v10-1_5b_r5/Src/'
BASE=sys.argv[2] if len(sys.argv)>2 else 'TME_App_Source/v10-1_5b_r42count_studio/Src/'
def rd(fn): return open(B+fn,encoding='utf-8',newline='').read()
def wr(fn,s): open(B+fn,'w',encoding='utf-8',newline='').write(s)
FILES=[f for f in sorted(os.listdir(B)) if f.endswith('.pa.yaml') and not f.startswith('_')]
def glob(o,n,expect):
    tot=0
    for f in FILES:
        s=rd(f); c=s.count(o)
        if c: tot+=c; wr(f,s.replace(o,n))
    assert tot==expect,(o[:70],tot,expect)
OID='Substitute(Text(User().EntraObjectId),"-","")'
WIN='DateAdd(Today(),-Coalesce(varCountWindowDaysV22,2),TimeUnit.Days)'
BADP='Error({Kind:ErrorKind.Validation,Message:"Тооллогын кэшийг бэлдэж чадсангүй. Хуучин файлыг дарж бичсэнгүй."})'
# H write: the payload is built and validated first; SaveData runs only on a valid array
HWRITE=('With({_h22:JSON(FirstN(SortByColumns(Filter(colOfflineInventory,Synced),"CountDate",SortOrder.Descending),1000),JSONFormat.Compact)},'
        'If(IsError(_h22) || Left(_h22,1)<>"[" || Right(_h22,1)<>"]",'+BADP+','
        'ClearCollect(colCountHistDiskV22,{Schema:22,Owner:varCountOwner,Payload:_h22});'
        'SaveData(colCountHistDiskV22,"C22H" & '+OID+');Set(varCountHistDiskAtV22,Now())))')
# G1: every device write = unsent rows only (16 sites)
glob('{Schema:21,Owner:varCountOwner,Payload:JSON(colOfflineInventory,JSONFormat.Compact)}',
     '{Schema:22,Owner:varCountOwner,Payload:JSON(Filter(colOfflineInventory,!Synced),JSONFormat.Compact)}',16 if 'varCountAppendReadyR42' not in rd('scrWarehouses.pa.yaml') else 15)
# Button1_2 (Codex append path, TEST_1 only): the payload is now only the unsent rows, so the append shortcut is no longer needed
s=rd('scrWarehouses.pa.yaml')
m=None if 'varCountAppendReadyR42' not in s else re.search(r'With\(\{payload:If\(Coalesce\(varCountAppendReadyR42,false\) &&.*?JSON\(colOfflineInventory,JSONFormat\.Compact\)\)\},',s,re.S)
if m:
  assert s.count('{Schema:21,Owner:varCountOwner,Payload:payload}')==1
  s=s[:m.start()]+'With({payload:JSON(Filter(colOfflineInventory,!Synced),JSONFormat.Compact)},'+s[m.end():]
  s=s.replace('{Schema:21,Owner:varCountOwner,Payload:payload}','{Schema:22,Owner:varCountOwner,Payload:payload}')
  wr('scrWarehouses.pa.yaml',s)
# G1b: P write: build + validate the payload before replacing the envelope or calling SaveData
tot=0
for f in FILES:
    t=rd(f)
    t,c=re.subn(r'ClearCollect\(colCountDiskV21,\{Schema:22,Owner:varCountOwner,Payload:JSON\(Filter\(colOfflineInventory,!Synced\),JSONFormat\.Compact\)\}\);(\s*)SaveData\(colCountDiskV21,varCountCacheKey\)',
        lambda m:'With({_p22:JSON(Filter(colOfflineInventory,!Synced),JSONFormat.Compact)},If(IsError(_p22) || Left(_p22,1)<>"[" || Right(_p22,1)<>"]",'+BADP+','
                 'ClearCollect(colCountDiskV21,{Schema:22,Owner:varCountOwner,Payload:_p22});'+m.group(1)+'SaveData(colCountDiskV21,varCountCacheKey)))',t)
    if c: tot+=c; wr(f,t)
assert tot==16 or ('varCountAppendReadyR42' in rd('scrWarehouses.pa.yaml') and tot==15),tot
# G2: restore only the window from SharePoint (6 sites)
glob("Filter(InventoryCount,Counter=varCountOwner || (Counter=User().FullName && 'Created By'.Email=varCountOwner))",
     "Filter(InventoryCount,(Counter=varCountOwner || (Counter=User().FullName && 'Created By'.Email=varCountOwner)) && Created>="+WIN+")",6)
# G3: after each restore merge: drop sent rows outside the window, persist H (never when the device store was not read safely)
glob('ClearCollect(colOfflineInventory,DropColumns(colHistoryMergedV16,MergePriority));',
     'ClearCollect(colOfflineInventory,DropColumns(colHistoryMergedV16,MergePriority));'
     'RemoveIf(colOfflineInventory,Synced && !IsBlank(CountDate) && CountDate<'+WIN+');'
     'If(varCountDiskSafeV21,IfError('+HWRITE+',Set(varCountHistDiskErrorV22,FirstError.Message)));',6)
# App.OnStart loader
s=rd('App.pa.yaml')
def rep(s,o,n,c=1):
    assert s.count(o)==c,(o[:80],s.count(o)); return s.replace(o,n)
s=rep(s,'Set(varCountCacheKey,"C21" & '+OID+');',
 'Set(varCountCacheKey,"C22P" & '+OID+');Set(varCountHistKeyV22,"C22H" & '+OID+');Set(varCountLegacyKeyV22,"C21" & '+OID+');'
 'Set(varCountMigrateV22,false);Set(varCountWindowDaysV22,2);Set(varCountHistDiskErrorV22,"");'
 'ClearCollect(colCountHistDiskV22,{Schema:22,Owner:"",Payload:"[]"});Clear(colCountHistDiskV22);')
if 'If(IsError(LoadData(colCountDiskV21,varCountCacheKey,true)),' in s:
 s=rep(s,'      If(IsError(LoadData(colCountDiskV21,varCountCacheKey,true)),\n',
 '      Set(varCountLoadFailV22,IsError(LoadData(colCountDiskV21,varCountCacheKey,true)));\n'
 '      If(!varCountLoadFailV22 && IsEmpty(colCountDiskV21),Set(varCountLoadFailV22,IsError(LoadData(colCountDiskV21,varCountLegacyKeyV22,true)));Set(varCountMigrateV22,!varCountLoadFailV22 && !IsEmpty(colCountDiskV21)));\n'
 '      If(varCountLoadFailV22,\n')
 s=rep(s,'CountRows(colCountDiskV21)<>1 || First(colCountDiskV21).Schema<>21 ||',
        'CountRows(colCountDiskV21)<>1 || First(colCountDiskV21).Schema<>If(varCountMigrateV22,21,22) ||')
else:
 m=re.search(r'\n(\s*)LoadData\(colCountDiskV21,varCountCacheKey,true\);\n',s); assert m
 s=s[:m.end()]+m.group(1)+'If(IsEmpty(colCountDiskV21),LoadData(colCountDiskV21,varCountLegacyKeyV22,true);Set(varCountMigrateV22,!IsEmpty(colCountDiskV21)));\n'+s[m.end():]
 s=rep(s,'If(First(colCountDiskV21).Schema<>21 || First(colCountDiskV21).Owner<>varCountOwner,',
        'If(First(colCountDiskV21).Schema<>If(varCountMigrateV22,21,22) || First(colCountDiskV21).Owner<>varCountOwner,')
# reuse the exact row mapping for H
m=re.search(r'ClearCollect\(colOfflineInventory,ForAll\(Table\(ParseJSON\(First\(colCountDiskV21\)\.Payload\)\) As r,(\{.*?Synced:Boolean\(r\.Value\.Synced\)\})\)\)',s,re.S)
assert m; MAP=m.group(1)
HLOAD=('\n       If(!varCountMigrateV22,IfError(LoadData(colCountHistDiskV22,varCountHistKeyV22,true);'
 'If(!IsEmpty(colCountHistDiskV22) && First(colCountHistDiskV22).Schema=22 && First(colCountHistDiskV22).Owner=varCountOwner,'
 'ClearCollect(colCountHistRowsV22,ForAll(Table(ParseJSON(First(colCountHistDiskV22).Payload)) As r,'+MAP+'));'
 'ClearCollect(colCountHistAddV22,Filter(colCountHistRowsV22,!(SyncKey in colOfflineInventory.SyncKey)));'
 'Collect(colOfflineInventory,colCountHistAddV22);Clear(colCountHistRowsV22);Clear(colCountHistAddV22));Clear(colCountHistDiskV22),'
 'Clear(colCountHistDiskV22);Set(varCountHistDiskErrorV22,FirstError.Message)));'
 '\n       RemoveIf(colOfflineInventory,Synced && !IsBlank(CountDate) && CountDate<'+WIN+')\n')
s=rep(s,'\n      If(varCountDiskSafeV21,\n       // v3.6.8: set-based merge','\n      If(varCountDiskSafeV21,'+HLOAD+'      );\n      If(varCountDiskSafeV21,\n       // v3.6.8: set-based merge')
s=rep(s,'If(varPerfPrevCandidatesV368=0 && !IsEmpty(colCountDiskV21),Set(varCountCacheReady,true)',
        'If(varPerfPrevCandidatesV368=0 && !IsEmpty(colCountDiskV21) && !varCountMigrateV22,Set(varCountCacheReady,true)')
s=rep(s,'Clear(colPreviousCountV21);\n      Set(varCountLoadDoneV21,true);',
 'Clear(colPreviousCountV21);\n'
 '      // r5: legacy V19 rows merged above can be old: keep only unsent rows and the window in memory\n'
 '      RemoveIf(colOfflineInventory,Synced && !IsBlank(CountDate) && CountDate<'+WIN+');\n'
 '      // r5: one-time C21 -> C22 migration. C21 is cleared only after P (above) and H were written.\n'
 '      If(varCountMigrateV22 && varCountDiskSafeV21 && varCountCacheReady,IfError('+HWRITE+';'
 # read P back and compare the unsent row count before C21 is removed
 'ClearCollect(colCountVerifyV22,{Schema:22,Owner:"",Payload:"[]"});Clear(colCountVerifyV22);LoadData(colCountVerifyV22,varCountCacheKey,true);'
 'If(CountRows(colCountVerifyV22)=1 && First(colCountVerifyV22).Schema=22 && First(colCountVerifyV22).Owner=varCountOwner && '
 'CountRows(Table(ParseJSON(First(colCountVerifyV22).Payload)))=CountRows(Filter(colOfflineInventory,!Synced)),'
 'ClearData(varCountLegacyKeyV22);Set(varCountMigrateV22,false),'
 'Set(varCountHistDiskErrorV22,"C22P буцааж уншихад таарсангүй; C21-ийг устгаагүй."));Clear(colCountVerifyV22),'
 'Set(varCountHistDiskErrorV22,FirstError.Message)));\n'
 '      Set(varCountLoadDoneV21,true);')
wr('App.pa.yaml',s)
# upload timers: when the queue is empty, persist H at most every 10 minutes
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
# checks + PASTE
def bal(f):
    f=re.sub(r'//[^\n]*','',f); f=re.sub(r'"[^"]*"','""',f); f=re.sub(r"'[^']*'","''",f); return (f.count('(')-f.count(')'),f.count('{')-f.count('}'))
R=BASE; out='TME_App_Source/v10-1_5b_r5/PASTE/'; n=0
for fn in FILES:
    a=props(open(R+fn,encoding='utf-8').read()); b=props(rd(fn))
    for key in b:
        if a.get(key)!=b[key]:
            assert bal(b[key])==(0,0),(key,bal(b[key])); n+=1
            ctl,prop=key.rsplit('.',1)
            open(f'{out}{n:02d}_{fn[:-8]}_{ctl}_{prop}.txt','w',encoding='utf-8').write(b[key][1:]); print(n,key,len(b[key]))
allsrc=''.join(rd(f) for f in FILES)
print('JSON(colOfflineInventory full:',allsrc.count('JSON(colOfflineInventory,'),'| Schema:21 left:',allsrc.count('Schema:21'))
