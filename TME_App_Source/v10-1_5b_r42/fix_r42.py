# r4 -> r4.2: TEST perf result no longer a banner over search; success banner 2 s;
# combined report splits a full day into hours (500 counts/day per warehouse no longer fails)
# run from repo root: python3 TME_App_Source/v10-1_5b_r42/fix_r42.py <dir with props.py>
import os,sys,re
sys.path.insert(0,sys.argv[1]); from props import props
B='TME_App_Source/v10-1_5b_r42/Src/'
def rd(fn): return open(B+fn,encoding='utf-8',newline='').read()
def wr(fn,s): open(B+fn,'w',encoding='utf-8',newline='').write(s)
def edit(fn,pairs):
    s=rd(fn)
    for o,n,c in pairs:
        assert s.count(o)==c,(fn,o[:80],s.count(o)); s=s.replace(o,n)
    wr(fn,s)
# A. Button1_2: perf summary -> variables shown on the chip, no banner
s=rd('scrWarehouses.pa.yaml')
a0='Notify("ХУРД #" & Last(colPerfSumV1015).Block'; a1=',NotificationType.Information);Clear(colPerfV1015);'
assert s.count(a0)==1
i=s.index(a0); j=s.index(a1,i); msg=s[i+len('Notify('):j]
s=s[:i]+('Set(varPerfLastMsgV1015,'+msg+');'
 'Set(varPerfShortV1015,"⏱ " & Text(Last(colPerfSumV1015).MedianMs/1000,"0.0","en-US") & "/" & Text(Last(colPerfSumV1015).P95Ms/1000,"0.0","en-US") & "с");'
 'Clear(colPerfV1015);')+s[j+len(a1):]
wr('scrWarehouses.pa.yaml',s)
edit('scrWarehouses.pa.yaml',[
 # success banner 2 s (errors keep the default)
 ('"Төхөөрөмжид хадгаллаа · интернет ормогц автоматаар илгээнэ."),If(varCountCloudOnlyV21,NotificationType.Warning,NotificationType.Success))',
  '"Төхөөрөмжид хадгаллаа · интернет ормогц автоматаар илгээнэ."),If(varCountCloudOnlyV21,NotificationType.Warning,NotificationType.Success),2000)',1),
 # B. chip "Локал · N": TEST shows median/P95; first tap shows the full line once, next tap opens the menu as before
 ('Text: ="Локал · " & CountRows(Filter(colOfflineInventory,OwnerEmail=varCountOwner && !Synced',
  'Text: =If(Coalesce(varPerfDiagV1015,false) && !IsBlank(varPerfShortV1015),varPerfShortV1015,"Локал · " & CountRows(Filter(colOfflineInventory,OwnerEmail=varCountOwner && !Synced',1),
 ])
# OnSelect exists on two controls: change it only inside the phoneCountLocal block
s=rd('scrWarehouses.pa.yaml'); b0=s.index('      - phoneCountLocal:\n'); b1=s.index('\n      - ',b0+10); blk=s[b0:b1]
o='OnSelect: =Set(varCountMenuV21,true);SetFocus(countMenuItemV21_0)'; assert blk.count(o)==1
blk=blk.replace(o,'OnSelect: =If(Coalesce(varPerfDiagV1015,false) && !IsBlank(varPerfLastMsgV1015),Notify(varPerfLastMsgV1015,NotificationType.Information,6000);Set(varPerfLastMsgV1015,Blank()),Set(varCountMenuV21,true);SetFocus(countMenuItemV21_0))')
wr('scrWarehouses.pa.yaml',s[:b0]+blk+s[b1:])
s=rd('scrWarehouses.pa.yaml')
k=s.index('Text: =If(Coalesce(varPerfDiagV1015,false) && !IsBlank(varPerfShortV1015)'); e=s.index('\n',k)
wr('scrWarehouses.pa.yaml',s[:e]+')'+s[e:])
# C. combined report slicing: >1 day -> days, 1 day -> hours, only a full 1-hour slice fails
edit('ScrCombined.pa.yaml',[
 ('If(DateDiff(pgReadStart4f,pgReadStop4f,TimeUnit.Days)>1,','If(DateDiff(pgReadStart4f,pgReadStop4f,TimeUnit.Hours)>1,',1),
 ('Collect(colPgSlices4f,ForAll(Sequence(DateDiff(pgReadStart4f,pgReadStop4f,TimeUnit.Days)) As dayNo,',
  'With({step4f:If(DateDiff(pgReadStart4f,pgReadStop4f,TimeUnit.Hours)>24,24,1)},Collect(colPgSlices4f,ForAll(Sequence(RoundUp(DateDiff(pgReadStart4f,pgReadStop4f,TimeUnit.Hours)/step4f,0)) As dayNo,',1),
 ('{startAt:DateAdd(pgReadStart4f,dayNo.Value-1,TimeUnit.Days),','{startAt:DateAdd(pgReadStart4f,(dayNo.Value-1)*step4f,TimeUnit.Hours),',1),
 ('stopAt:DateAdd(pgReadStart4f,dayNo.Value,TimeUnit.Days),place:pgReadPlace4f}));true,',
  'stopAt:Min(pgReadStop4f,DateAdd(pgReadStart4f,dayNo.Value*step4f,TimeUnit.Hours)),place:pgReadPlace4f})));true,',1),
 ('"Нэг өдрийн 500 мөрийн хязгаарт хүрсэн тул тайланг бүрэн харуулах боломжгүй."','"Нэг цагт 500-аас олон мөр тул тайланг бүрэн харуулах боломжгүй."',1)])
def bal(f):
    f=re.sub(r'//[^\n]*','',f); f=re.sub(r'"[^"]*"','""',f); f=re.sub(r"'[^']*'","''",f); return (f.count('(')-f.count(')'),f.count('{')-f.count('}'))
R='TME_App_Source/v10-1_5b_r4/Src/'; out='TME_App_Source/v10-1_5b_r42/PASTE/'; n=0
for fn in ['scrWarehouses.pa.yaml','ScrCombined.pa.yaml']:
    a=props(open(R+fn,encoding='utf-8').read()); b=props(rd(fn))
    for key in b:
        if a[key]!=b[key]:
            assert bal(b[key])==(0,0),(key,bal(b[key])); n+=1
            ctl,prop=key.rsplit('.',1)
            open(f'{out}{n:02d}_{fn[:-8]}_{ctl}_{prop}.txt','w',encoding='utf-8').write(b[key][1:]); print(n,key)
