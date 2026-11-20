import os,sys
sys.path.insert(0,os.path.dirname(__file__)); from props import props
D='TME_App_Source/v10-1_5b/Src'
def rw(fn,pairs):
    p=os.path.join(D,fn); s=open(p,encoding='utf-8',newline='').read()
    for o,n,c in pairs:
        got=s.count(o); assert got==c,(fn,o[:80],got,c); s=s.replace(o,n)
    open(p,'w',encoding='utf-8',newline='').write(s)
# (2) Refresh failure must stop the report from being marked ready; (5) DIAG only via the test switch
rw('ScrCombined.pa.yaml',[
 ('IfError(Refresh(InventoryCount),false);',
  'Set(pgRefreshOkV1015,IfError(Refresh(InventoryCount);true,false));'
  'If(!pgRefreshOkV1015,Notify("SharePoint-оос тайлангийн өгөгдлийг шинэчилж чадсангүй. Тайланг бэлэн гэж тооцохгүй.",NotificationType.Error));',4),
 ('Clear(pgRaw);Set(pgReportReady,true)','Clear(pgRaw);Set(pgReportReady,pgRefreshOkV1015)',4),
 ('If(Coalesce(varPerfDiagV1015,false) || Lower(User().Email)="od.u@tme.mn",','If(Coalesce(varPerfDiagV1015,false),',4),
 ('OnVisible: |-\n        =','OnVisible: |-\n        =Set(varPerfDiagV1015,true);',1)])
# (3) true median of 20; (4) persist the perf log only every 20th save, after the summary
rw('scrWarehouses.pa.yaml',[
 ('IfError(SaveData(colPerfV1015,"PerfV1015_" & Substitute(Text(User().EntraObjectId),"-","")),false);'
  'If(Mod(CountRows(colPerfV1015),20)=0,With({w:Sort(LastN(colPerfV1015,20),TotalMs)},'
  'Notify("ХУРД · сүүлийн 20 хадгалалт: медиан " & Index(w,10).TotalMs & " мс,',
  'If(Mod(CountRows(colPerfV1015),20)=0,With({w:Sort(LastN(colPerfV1015,20),TotalMs)},'
  'Notify("ХУРД · сүүлийн 20 хадгалалт: медиан " & (Index(w,10).TotalMs+Index(w,11).TotalMs)/2 & " мс,',1),
 ('түүх " & Last(colPerfV1015).HistoryRows & " мөр",NotificationType.Information))))',
  'түүх " & Last(colPerfV1015).HistoryRows & " мөр",NotificationType.Information));'
  'IfError(SaveData(colPerfV1015,"PerfV1015_" & Substitute(Text(User().EntraObjectId),"-","")),false)))',1)])
print('ok')
