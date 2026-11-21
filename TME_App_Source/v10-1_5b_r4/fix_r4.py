# r3 -> r4: one diag switch in App.OnStart; perf log = small per-20 summary, persist time measured separately
import os,sys,re
sys.path.insert(0,sys.argv[1]); from props import props
B='TME_App_Source/v10-1_5b_r4/Src/'
def edit(fn,pairs):
    s=open(B+fn,encoding='utf-8',newline='').read()
    for o,n,c in pairs:
        assert s.count(o)==c,(fn,o[:70],s.count(o)); s=s.replace(o,n)
    open(B+fn,'w',encoding='utf-8',newline='').write(s)
SW='Set(varPerfDiagV1015,true);'
edit('ScrCombined.pa.yaml',[('With({entryTicket:pgRun4f},'+SW,'With({entryTicket:pgRun4f},',1)])
edit('scrWarehouses.pa.yaml',[('=Set(varPerfDiagV1015,true);If(IsBlank(varCountReceiptV369.SyncKey)','=If(IsBlank(varCountReceiptV369.SyncKey)',1)])
OLD=('If(Mod(CountRows(colPerfV1015),20)=0,With({w:Sort(LastN(colPerfV1015,20),TotalMs)},Notify("ХУРД · сүүлийн 20 хадгалалт: медиан " & (Index(w,10).TotalMs+Index(w,11).TotalMs)/2 & " мс, хамгийн удаан " & Last(w).TotalMs & " мс (локал бичилт " & Max(w,LocalMs) & " мс), түүх " & Last(colPerfV1015).HistoryRows & " мөр",NotificationType.Information));!IsError(SaveData(colPerfV1015,"PerfV1015_" & Substitute(Text(User().EntraObjectId),"-",""))))')
NEW=('If(CountRows(colPerfV1015)>=20,With({w:Sort(LastN(colPerfV1015,20),TotalMs),k:"PerfSumV1015_" & Substitute(Text(User().EntraObjectId),"-","")},'
 # read the earlier log into a temp collection; only a successful read unlocks writing to the key
 'If(!Coalesce(varPerfSumLoadedV1015,false),If(false,ClearCollect(colPerfSumLoadV1015,colPerfSumV1015));Clear(colPerfSumLoadV1015);'
 'If(IfError(LoadData(colPerfSumLoadV1015,k,true);true,false),'
 'ClearCollect(colPerfSumMemV1015,colPerfSumV1015);ClearCollect(colPerfSumV1015,colPerfSumLoadV1015);'
 'Collect(colPerfSumV1015,ForAll(Sequence(CountRows(colPerfSumMemV1015)) As n,Patch(Index(colPerfSumMemV1015,n.Value),{Block:CountRows(colPerfSumLoadV1015)+n.Value})));'
 'Clear(colPerfSumMemV1015);Clear(colPerfSumLoadV1015);Set(varPerfSumLoadedV1015,true),'
 'Clear(colPerfSumLoadV1015)));'
 'Collect(colPerfSumV1015,{Block:CountRows(colPerfSumV1015)+1,At:Now(),HistoryRows:Last(colPerfV1015).HistoryRows,MedianMs:(Index(w,10).TotalMs+Index(w,11).TotalMs)/2,P95Ms:Index(w,19).TotalMs,MaxMs:Last(w).TotalMs,LocalMaxMs:Max(w,LocalMs),PrevPersistMs:varPerfPersistMsV1015});'
 'Notify("ХУРД #" & Last(colPerfSumV1015).Block & " · түүх " & Last(colPerfSumV1015).HistoryRows & " мөр · 20 хадгалалт: медиан " & Last(colPerfSumV1015).MedianMs & " мс, P95 " & Last(colPerfSumV1015).P95Ms & " мс, max " & Last(colPerfSumV1015).MaxMs & " мс, локал max " & Last(colPerfSumV1015).LocalMaxMs & " мс · өмнөх лог бичилт " & If(IsBlank(varPerfPersistMsV1015),"-",varPerfPersistMsV1015=-2,"ХИЙГДЭЭГҮЙ (хуучин логийг уншиж чадаагүй тул дарж бичсэнгүй)",varPerfPersistMsV1015<0,"АЛДАА",Text(varPerfPersistMsV1015) & " мс"),NotificationType.Information);'
 'Clear(colPerfV1015);Set(varPerfT2V1015,Now());'
 'If(Coalesce(varPerfSumLoadedV1015,false),If(IsError(SaveData(colPerfSumV1015,k)),Set(varPerfPersistMsV1015,-1),Set(varPerfPersistMsV1015,DateDiff(varPerfT2V1015,Now(),TimeUnit.Milliseconds))),Set(varPerfPersistMsV1015,-2))))')
edit('scrWarehouses.pa.yaml',[(OLD,NEW,1)])
# single switch: first statement of App.OnStart (TEST = true, production = false)
s=open(B+'App.pa.yaml',encoding='utf-8',newline='').read()
m=re.search(r'(\n\s*OnStart: \|-?\s*\n(\s*)=)',s); assert m,'OnStart'
s=s[:m.end()]+'Set(varPerfDiagV1015,true); // TEST: true · PRODUCTION: false (ганц унтраалга)\n'+m.group(2)+s[m.end():]
open(B+'App.pa.yaml','w',encoding='utf-8',newline='').write(s)
def bal(f):
    f=re.sub(r'//[^\n]*','',f); f=re.sub(r'"[^"]*"','""',f); f=re.sub(r"'[^']*'","''",f); return (f.count('(')-f.count(')'),f.count('{')-f.count('}'))
R='TME_App_Source/v10-1_5b_r3_studio/Src/'; out='TME_App_Source/v10-1_5b_r4/PASTE/'; i=0
for fn in ['App.pa.yaml','ScrCombined.pa.yaml','scrWarehouses.pa.yaml']:
    a=props(open(R+fn,encoding='utf-8').read()); b=props(open(B+fn,encoding='utf-8').read())
    for k in b:
        if a[k]!=b[k]:
            assert bal(b[k])==(0,0),(k,bal(b[k])); i+=1
            ctl,prop=k.rsplit('.',1)
            open(f'{out}{i:02d}_{fn[:-8]}_{ctl}_{prop}.txt','w',encoding='utf-8').write(b[k][1:]); print(i,k,len(b[k]))
allsrc=''.join(open(B+f,encoding='utf-8').read() for f in os.listdir(B))
print('switch count', allsrc.count('Set(varPerfDiagV1015,true)'), 'old perf file', allsrc.count('"PerfV1015_"'))
