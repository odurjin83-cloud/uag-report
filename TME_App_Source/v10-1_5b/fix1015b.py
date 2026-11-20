import os,sys,re
D=sys.argv[1]
def load(fn): return open(os.path.join(D,fn),encoding='utf-8',newline='').read()
def save(fn,s): open(os.path.join(D,fn),'w',encoding='utf-8',newline='').write(s)
def rw(fn,pairs):
    s=load(fn)
    for o,n,c in pairs:
        got=s.count(o); assert got==c,(fn,o[:80],got,c); s=s.replace(o,n)
    save(fn,s)
def wrap_text_fmt(s,lit,builder,need_unguarded=True,expect=None):
    """Rewrite Text(EXPR,"lit") -> builder(EXPR) for each occurrence."""
    n=0; i=0
    while True:
        p=s.find(',"'+lit+'")',i)
        if p<0: break
        if need_unguarded and 'Mod(' in s[max(0,p-200):p]: i=p+1; continue
        # scan left for matching Text(
        depth=0; j=p-1; ins=False
        while j>=0:
            ch=s[j]
            if ch=='"': ins=not ins
            elif not ins:
                if ch==')': depth+=1
                elif ch=='(':
                    if depth==0: break
                    depth-=1
            j-=1
        assert s[j-4:j]=='Text',(lit,s[j-20:j+5])
        expr=s[j+1:p]; end=p+len(',"'+lit+'")')
        new=builder(expr); s=s[:j-4]+new+s[end:]; i=j-4+len(new); n+=1
    if expect is not None: assert n==expect,(lit,n,expect)
    return s

# ---------- 1. Warehouse permission leaks (camera search, item photos) ----------
P='!IsBlank(locationCode) && (Lower(User().Email)="od.u@tme.mn" || pgAccess.LocationCode="*" || ("|" & Upper(locationCode) & "|") in pgAccess.LocationCode)'
rw('ScrCameraSearch.pa.yaml',[
 ('Filter(colOfflineStock,itemNo=i.number)','Filter(colOfflineStock,itemNo=i.number && '+P+')',1),
 ('Filter(colOfflineStock,itemNo=ThisItem.number)','Filter(colOfflineStock,itemNo=ThisItem.number && '+P+')',1),
 ('Filter(colOfflineStock,itemNo=varCItem)','Filter(colOfflineStock,itemNo=varCItem && '+P+')',2)])
rw('ScrItemPhotos.pa.yaml',[('Filter(colOfflineStock,itemNo=varPhotoItemV28 && !IsBlank(locationCode))','Filter(colOfflineStock,itemNo=varPhotoItemV28 && '+P+')',1)])

# ---------- 2. Percent / number formats ----------
pct=lambda dec: (lambda e: 'Text(100*('+e+'),"'+dec+'") & "%"')
s=load('ScrReport1.pa.yaml')
s=wrap_text_fmt(s,'0.0%',pct('0.0'),False,1)          # rptHeroValue
s=wrap_text_fmt(s,'0%',pct('0'),False,1)              # rptCoverageVal
s=wrap_text_fmt(s,'+#,##0.##;-#,##0.##;0',lambda e:'With({_nfmt:'+e+'},If(_nfmt>0,"+","") & Text(_nfmt,If(Mod(_nfmt,1)=0,"#,##0","#,##0.##")))',False,6)
save('ScrReport1.pa.yaml',s)
s=load('ScrCombined.pa.yaml'); s=wrap_text_fmt(s,'0.0%',pct('0.0'),False,2); save('ScrCombined.pa.yaml',s)   # pgKpi1, pgKpi4
s=load('scrWarehouses.pa.yaml'); s=wrap_text_fmt(s,'0.###',lambda e:'With({_nfmt:'+e+'},Text(_nfmt,If(Mod(_nfmt,1)=0,"0","0.###")))',True,2); save('scrWarehouses.pa.yaml',s)

# ---------- 3. Combined report: fresh read + diagnostics ----------
DIAG=('If(Coalesce(varPerfDiagV1015,false) || Lower(User().Email)="od.u@tme.mn",'
      'Notify("ДИАГ · SharePoint-оос уншсан: " & CountRows(pgRaw) & " мөр (өнөөдөр " & CountRows(Filter(pgRaw,Created>=Today())) & "), тайланд орсон: " & CountRows(pgRows) & " · ID " & Min(pgRaw,ID) & "–" & Max(pgRaw,ID),NotificationType.Information));')
rw('ScrCombined.pa.yaml',[
 ('IfError(ForAll(Sequence(DateDiff(pgFrom','IfError(Refresh(InventoryCount),false);IfError(ForAll(Sequence(DateDiff(pgFrom',4),
 ('Clear(pgRaw);Set(pgReportReady,true)',DIAG+'Clear(pgRaw);Set(pgReportReady,true)',4)])

# ---------- 4. In-app save timing (test builds) ----------
rw('scrWarehouses.pa.yaml',[
 ('=If(!IsBlank(varCountReceiptV369.SyncKey),If(!((Lower(User()',
  '=Set(varPerfT0V1015,Now());Set(varPerfT1V1015,Blank());If(!IsBlank(varCountReceiptV369.SyncKey),If(!((Lower(User()',1),
 ('Set(varCountCacheReady,true);Set(varCountStorageError,"");Set(varCountSavedV21,true));',
  'Set(varCountCacheReady,true);Set(varCountStorageError,"");Set(varCountSavedV21,true);Set(varPerfT1V1015,Now()));',1),
 (',Notify("Энэ агуулахад тооллого хадгалах эрхгүй.",NotificationType.Error)))',
  ',Notify("Энэ агуулахад тооллого хадгалах эрхгүй.",NotificationType.Error)));'
  'If(Coalesce(varPerfDiagV1015,false) && !IsBlank(varPerfT1V1015),'
  'Collect(colPerfV1015,{At:varPerfT0V1015,LocalMs:DateDiff(varPerfT0V1015,varPerfT1V1015,TimeUnit.Milliseconds),TotalMs:DateDiff(varPerfT0V1015,Now(),TimeUnit.Milliseconds),HistoryRows:CountRows(colOfflineInventory)});'
  'IfError(SaveData(colPerfV1015,"PerfV1015_" & Substitute(Text(User().EntraObjectId),"-","")),false);'
  'If(Mod(CountRows(colPerfV1015),20)=0,With({w:Sort(LastN(colPerfV1015,20),TotalMs)},'
  'Notify("ХУРД · сүүлийн 20 хадгалалт: медиан " & Index(w,10).TotalMs & " мс, хамгийн удаан " & Last(w).TotalMs & " мс (локал бичилт " & Max(w,LocalMs) & " мс), түүх " & Last(colPerfV1015).HistoryRows & " мөр",NotificationType.Information))))',1)])
# TEST flag: on in this build; set to false before production
rw('scrWarehouses.pa.yaml',[('OnVisible: |-\n        =','OnVisible: |-\n        =Set(varPerfDiagV1015,true);',1)])
print('ok')
