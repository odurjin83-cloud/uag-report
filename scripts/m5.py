import pandas as pd,re,warnings;warnings.filterwarnings('ignore')
exec(open('m4.py').read().replace("out='/home/user","out='/tmp/claude-0/s/_o4.xlsx';_x='").replace("print(","(lambda *a,**k:None)("))
E1=pd.read_excel('/root/.claude/uploads/c075caec-a9e6-5da1-b896-4916865d4165/9606f590-_____________________________________________123456789101112-_________export_1790929690128.xlsx',dtype=str).assign(Эх='Баримт')
E2=pd.read_excel('/root/.claude/uploads/c075caec-a9e6-5da1-b896-4916865d4165/bd87214a-__________undefined__123456789101112_______export_1790929758621.xlsx',dtype=str)
E2=E2[E2['Толгой нэхэмжлэхийн ДДТД'].isna()].assign(Эх='Нэхэмжлэх')
E=pd.concat([E1,E2]); E['ed']=pd.to_datetime(E.Огноо).dt.date; E['amt']=E['Нийт дүн'].astype(float).round(2); E=E[E.amt>0]
E['TTD']=E['Харилцагчийн ТТД'].str.strip()
print('ebarimt',E.Эх.value_counts().to_dict(),E.ed.min(),E.ed.max(),'BC vendor-т байгаа ТТД',f"{E.TTD.isin(VN).mean():.0%}")
X=S[['sid','d','amt','cpn','desc','BC_код','Итгэл','Дүрэм']].merge(E[['TTD','ed','amt','ДДТД','Харилцагчийн нэр','Эх']],on='amt')
X['lag']=(pd.to_datetime(X.d)-pd.to_datetime(X.ed)).dt.days
X=X[(X.lag>=-30)&(X.lag<=90)]
X=X.sort_values('lag',key=abs).drop_duplicates(['sid','TTD'])
X['n']=X.groupby('sid').TTD.transform('nunique'); X=X[X.n==1].drop_duplicates('sid')
print('ebarimt-тай нэг утгатай тулгагдсан хуулга',len(X), X.Эх.value_counts().to_dict())
T=X.merge(M[['sid','Bal. Account No.']].drop_duplicates('sid'),on='sid')
T['base']=T['Bal. Account No.'].astype(str).str.replace('-UTT','')
print('ТТД = BC харилцагч:',f"{(T.TTD==T.base).mean():.1%}",'/',len(T))
T2=T[T.TTD==T.base].copy(); T2['UTT']=T2['Bal. Account No.'].astype(str).str.endswith('-UTT'); T2['Баримт_өмнө']=T2.lag>=0
print(pd.crosstab(T2.Баримт_өмнө,T2.UTT,margins=True))
print('Шалгах/Тодорхойгүй-с шийдэгдэх:',X[X.Итгэл=='Шалгах'].shape[0], X[X.Дүрэм=='Тодорхойгүй'].shape[0])
pd.to_pickle((X,E),'X.pkl')
T['ok']=T.TTD==T.base; T['lagb']=pd.cut(T.lag,[-31,-1,7,30,90])
print(T.groupby(['Эх','lagb']).ok.agg(['size','mean']).round(3))
X=X.merge(T[['sid']].assign(chk=1),on='sid',how='left')
# Дүрэмд нэмэх
xi=X.set_index('sid')
def upd(r):
    if r.sid not in xi.index: return r
    x=xi.loc[r.sid]; r['eb_ТТД']=x.TTD; r['eb_нэр']=x['Харилцагчийн нэр']; r['eb_огноо']=x.ed; r['eb_төрөл']=x.Эх
    base=str(r.BC_код).replace('-UTT','')
    if r.Дүрэм in ('Тодорхойгүй','Нэрээр') and x.TTD in VN:
        r['Акаунт_төрөл']='Vendor'; r['BC_код']=x.TTD; r['BC_нэр']=VN[x.TTD]; r['Дүрэм']='ebarimt ТТД'; r['Итгэл']='Шалгах' if abs(x.lag)>7 else 'Дунд'
    elif base and base==x.TTD and r.Итгэл=='Дунд': r['Итгэл']='Өндөр'; r['Дүрэм']+=' + ebarimt'
    elif base and base!=x.TTD and r.Итгэл!='Шалгах' and r.Акаунт_төрөл in('Vendor','Customer'): r['eb_тэмдэг']='ebarimt өөр ТТД'
    return r
S['eb_тэмдэг']='';S=S.apply(upd,axis=1)
T=S.merge(M[['sid','Bal. Account No.']].drop_duplicates('sid'),on='sid'); T['Зөв']=T.BC_код==T['Bal. Account No.'].astype(str)
bt=T.groupby(['Дүрэм','Итгэл']).agg(Тоо=('sid','size'),Зөв_хувь=('Зөв','mean')).reset_index().sort_values('Тоо',ascending=False); bt['Зөв_хувь']=bt.Зөв_хувь.round(3)
print(bt.to_string()); print('Бүх хуулга:',S.Итгэл.value_counts().to_dict())
cols+=['eb_тэмдэг','eb_ТТД','eb_нэр','eb_огноо','eb_төрөл']
out='/home/user/uag-report/Данс_BC_харилцагч_маплинг.xlsx'
# ebarimt-д байгаа ч BC vendor-т байхгүй ТТД
NE=E[~E.TTD.isin(VN)&~E.TTD.isin(CN)].groupby(['TTD','Харилцагчийн нэр']).agg(Тоо=('amt','size'),Дүн=('amt','sum')).reset_index().sort_values('Дүн',ascending=False)
with pd.ExcelWriter(out) as w:
    S[cols].to_excel(w,sheet_name='Автомат_санал',index=False); bt.to_excel(w,sheet_name='Нарийвчлал',index=False)
    R.to_excel(w,sheet_name='Маплинг',index=False); SB.to_excel(w,sheet_name='Данс+утга',index=False); U.to_excel(w,sheet_name='Утгын_дүрэм',index=False)
    pd.DataFrame(sorted(own.items()),columns=['Өөрийн_данс','BC_Bank']).to_excel(w,sheet_name='Өөрийн_данс',index=False)
    S[S.Итгэл=='Шалгах'][cols].to_excel(w,sheet_name='Шалгах',index=False)
    NE.to_excel(w,sheet_name='BC-д_байхгүй_ТТД',index=False)
    M[['Түвшин','file','k4','d','amt','cpn','cpname','desc','Document No.','Bal. Account No.','Cust/Vend Name','Type']].to_excel(w,sheet_name='Тулгалт',index=False)
print('BC-д байхгүй ТТД',len(NE))
