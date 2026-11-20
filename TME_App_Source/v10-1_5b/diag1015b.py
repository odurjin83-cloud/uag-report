import os,sys
sys.path.insert(0,os.path.dirname(__file__)); from props import props
fn='TME_App_Source/v10-1_5b/Src/ScrCombined.pa.yaml'
s=open(fn,encoding='utf-8',newline='').read()
OLD=('If(Coalesce(varPerfDiagV1015,false) || Lower(User().Email)="od.u@tme.mn",'
     'Notify("ДИАГ · SharePoint-оос уншсан: " & CountRows(pgRaw) & " мөр (өнөөдөр " & CountRows(Filter(pgRaw,Created>=Today())) & "), тайланд орсон: " & CountRows(pgRows) & " · ID " & Min(pgRaw,ID) & "–" & Max(pgRaw,ID),NotificationType.Information));')
IDS='5031,5033,5035,5036,5037,5039,5040,5041,5042,5043,5044,5045,5046,5047,5048,5049,5050,5052,5056,5057,5058,5078,5079,5081,5083,5085,5086,5088,5090,5092,5095,5097,5099,5101,5103,5105,5107,5109,5111,5113'
NEW=('If(Coalesce(varPerfDiagV1015,false) || Lower(User().Email)="od.u@tme.mn",'
     # TEST-only control set: Od (PLE110) CAMP counts saved 2026-11-20, IDs from TME-v36-device-check.md
     'With({ctl:ForAll(Split("'+IDS+'",",") As c,{Id:Value(c.Value)})},'
     'With({rd:Filter(ctl As c,c.Id in pgRaw.ID),kp:Filter(ctl As c,c.Id in pgRows.ID)},'
     'Notify("ДИАГ 2026-11-20 Од CAMP · уншсан " & CountRows(rd) & "/" & CountRows(ctl) & " · тайланд үлдсэн " & CountRows(kp) & "/" & CountRows(ctl)'
     ' & " · УНШААГҮЙ: " & Coalesce(Concat(Filter(ctl As c,!(c.Id in pgRaw.ID)),Text(Id),","),"-")'
     ' & " · ШҮҮЛТЭД ХАСАГДСАН: " & Coalesce(Concat(Filter(ctl As c,c.Id in pgRaw.ID && !(c.Id in pgRows.ID)),Text(Id),","),"-")'
     ' & " · нийт уншсан " & CountRows(pgRaw) & ", тайланд " & CountRows(pgRows),NotificationType.Information))));')
assert s.count(OLD)==4,s.count(OLD)
s=s.replace(OLD,NEW); open(fn,'w',encoding='utf-8',newline='').write(s)
# refresh paste files for the 4 ScrCombined props
p=props(s); out='TME_App_Source/v10-1_5b/PASTE'
for f in os.listdir(out):
    if f.startswith(('04_','07_','08_','09_')) and 'ScrCombined' in f:
        ctl,prop=f[:-4].split('ScrCombined_',1)[1].rsplit('_',1)
        open(os.path.join(out,f),'w',encoding='utf-8').write(p[ctl+'.'+prop][1:]); print('updated',f)
