import os,sys,re
sys.path.insert(0,os.path.dirname(__file__)); from props import props
fn='TME_App_Source/v10-1_5b/Src/ScrCombined.pa.yaml'
s=open(fn,encoding='utf-8',newline='').read()
MSG='"SharePoint-оос тайлангийн өгөгдлийг шинэчилж чадсангүй. Тайланг бэлэн гэж тооцохгүй."'
pairs=[
 # start reading only after a successful refresh; reset load flags first
 ('If(!pgRefreshOkV1015,Notify('+MSG+',NotificationType.Error));IfError(ForAll(Sequence(DateDiff(pgFrom',
  'Set(pgLoadedOkV1015,false);Set(pgReadFailV1015,false);If(!pgRefreshOkV1015,Notify('+MSG+',NotificationType.Error),IfError(ForAll(Sequence(DateDiff(pgFrom'),
 # inside the success branch only mark "all days loaded"; readiness is decided after IfError
 ('Clear(pgRaw);Set(pgReportReady,pgRefreshOkV1015)),Notify(FirstError.Message,NotificationType.Error))',
  'Clear(pgRaw);Set(pgLoadedOkV1015,true)),Set(pgReadFailV1015,true);Notify(FirstError.Message,NotificationType.Error)));'
  'Set(pgReportReady,pgRefreshOkV1015 && pgLoadedOkV1015 && !pgReadFailV1015)')]
for o,n in pairs:
    assert s.count(o)==4,(o[:60],s.count(o)); s=s.replace(o,n)
open(fn,'w',encoding='utf-8',newline='').write(s)
def bal(f):
    f=re.sub(r'//[^\n]*','',f); f=re.sub(r'"[^"]*"','""',f); f=re.sub(r"'[^']*'","''",f); return (f.count('(')-f.count(')'),f.count('{')-f.count('}'))
p=props(s); out='TME_App_Source/v10-1_5b/PASTE'
for f in sorted(os.listdir(out)):
    if f.endswith('.txt') and '_ScrCombined_' in f:
        ctl,prop=f[3:-4].split('ScrCombined_',1)[1].rsplit('_',1); v=p[ctl+'.'+prop]
        assert bal(v)==(0,0),(f,bal(v))
        if open(os.path.join(out,f),encoding='utf-8').read()!=v[1:]:
            open(os.path.join(out,f),'w',encoding='utf-8').write(v[1:]); print('updated',f)
k='pgPeriod0.OnSelect'; v=p[k]; i=v.find('Set(pgLoadedOkV1015,false)'); j=v.find('Set(pgReportReady,pgRefreshOkV1015 &&')
print(v[i:i+330]); print('...'); print(v[j-260:j+90])
