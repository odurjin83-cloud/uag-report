import pandas as pd,re,warnings;warnings.filterwarnings('ignore')
exec(open('m3.py').read().replace("out='/home/user","out='/tmp/claude-0/s/_old.xlsx';_x='"))
V=pd.read_excel('/root/.claude/uploads/c075caec-a9e6-5da1-b896-4916865d4165/8b2087c4-Vendors.xlsx',dtype={'No.':str}); C=pd.read_excel('/root/.claude/uploads/c075caec-a9e6-5da1-b896-4916865d4165/fe130017-Customers.xlsx',dtype={'No.':str})
B=pd.read_excel('/root/.claude/uploads/c075caec-a9e6-5da1-b896-4916865d4165/5a0aad15-Bank_Accounts_4.xlsx'); GL=pd.read_excel('/root/.claude/uploads/c075caec-a9e6-5da1-b896-4916865d4165/e09d172e-Chart_of_Accounts_18.xlsx',dtype={'No.':str})
VN=dict(zip(V['No.'],V.Name)); CN=dict(zip(C['No.'],C.Name)); BN=dict(zip(B['No.'],B.Name)); GN=dict(zip(GL['No.'],GL.Name))
def atype(c):
    c=str(c)
    return 'Vendor' if c in VN else 'Customer' if c in CN else 'Bank Account' if c in BN else 'G/L Account' if c in GN else ''
# өөрийн данснууд
own={}
for n,nm in zip(B['No.'],B.Name):
    for a in re.findall(r'\d{8,}',str(nm)): own[a.lstrip('0')]=n
for k4,n in [(str(n)[-4:],n) for n in B['No.']]: pass
OWNACC={'5060173760':'BANK3760','5038159891':'BANK9891','5111753588':'BANK3588','5060173512':'BANK3512','5060173782':'BANK3782',
 '1105040964':'BANK0964','1105040965':'BANK0965','8145102237':'BANK2237','8145102012':'BANK2012','8145102104':'BANK2104','8145100572':'BANK0572',
 '8145100573':'BANK0573','3005136914':'BANK6914','9005482046':'BANK2046','5006033202':'BANK3202','499563903':'BANK3903','499563904':'BANK3904',
 '340004336976':'BANK6976','40004342599':'SAVING2599','340004342599':'SAVING2599'}
own.update(OWNACC)
for a in ['3005164784','3005164785','3005164786','3005164787','3005164788','3005164789','3005164790','3005175419','3005175420','3005175421','2025165510','2025179278','2025179279']:
    c=[n for n in B['No.'] if str(n).startswith('DEBIT CARD') and str(n).endswith(a[-4:])]
    if c: own[a]=c[0]
def norm(s): return re.sub(r'\b(ХХК|ХК|LLC|ТӨХК|ТББ|ХЗХ|CO|LTD)\b|[^А-ЯӨҮЁA-Z0-9]','',str(s).upper())
NV={}
for k,n in VN.items(): NV.setdefault(norm(n),[]).append(k)
HU=M.assign(u=M['Bal. Account No.'].astype(str).str.endswith('-UTT')).groupby('cpn').u.mean().to_dict()
mp=R.set_index('Харьцсан_данс')
FEE=re.compile(r'charges|шимтгэл|хөтөлсний|fee',re.I)
def decide(r):
    d=str(r.desc); cp=str(r.cpn)
    if FEE.search(d) and r.amt<=20000: return ('G/L Account','7000-093','BANK FEE','Шимтгэл (гүйлгээ бүр)','Өндөр')
    if cp in own: return ('Bank Account',own[cp],'INTER-ACCOUNT','Өөрийн данс','Өндөр')
    if cp in mp.index:
        m=mp.loc[cp]; code=m.BC_код.replace('-UTT','')
        if m.UTT_хувилбартай=='Тийм' or code+'-UTT' in CN:
            if re.search(r'урьдчилгаа|\d+ ?%',d,re.I): return ('Customer',code+'-UTT',m.Type,'Данс + "урьдчилгаа"','Шалгах')
            if re.search(r'үлдэгдэл|нэхэмжлэх',d,re.I): return (atype(code) or 'Vendor',code,m.Type,'Данс + "үлдэгдэл"','Шалгах')
            h=HU.get(cp)
            if h is not None and h>=0.8: return ('Customer',code+'-UTT',m.Type,'Данс (түүхээр UTT ≥80%)','Дунд')
            if h is not None and h<=0.2: return (atype(code),code,m.Type,'Данс (түүхээр Vendor ≥80%)','Шалгах')
            return (atype(code),code,m.Type,'UTT/Vendor ялгах','Шалгах')
        if m.Төлөв=='Тодорхой' and m.ГҮ_тоо>=2: return (atype(m.BC_код),m.BC_код,m.Type,'Дансны түүх','Өндөр')
        if m.Төлөв in('Тодорхой','Давамгай'): return (atype(m.BC_код),m.BC_код,m.Type,'Дансны түүх (цөөн)','Дунд')
    for rd in re.findall(r'(?<!\d)(\d{7})(?!\d)',d):
        if rd in VN and rd!='5482046': return ('Vendor',rd,'','Утган дахь РД','Дунд')
    k=norm(r.cpname)
    if len(k)>=4 and len(NV.get(k,[]))==1: return ('Vendor',NV[k][0],'','Нэрээр','Шалгах')
    return ('','','','Тодорхойгүй','Шалгах')
S[['Акаунт_төрөл','BC_код','Type','Дүрэм','Итгэл']]=S.apply(lambda r:pd.Series(decide(r)),axis=1)
S['BC_нэр']=S.BC_код.map(lambda c: VN.get(c) or CN.get(c) or BN.get(c) or GN.get(c) or '')
# Backtest: тулгагдсан мөрүүд дээр BC-тэй харьцуулах
T=S.merge(M[['sid','Bal. Account No.']].drop_duplicates('sid'),on='sid')
T['Зөв']=T.BC_код==T['Bal. Account No.'].astype(str)
bt=T.groupby(['Дүрэм','Итгэл']).agg(Тоо=('sid','size'),Зөв_хувь=('Зөв','mean')).reset_index().sort_values('Тоо',ascending=False)
bt['Зөв_хувь']=bt.Зөв_хувь.round(3)
print(bt.to_string()); o=T[T.Дүрэм=='Өөрийн данс']; print(o[~o.Зөв][['BC_код','Bal. Account No.']].value_counts().head(8)); print('Хуулга бүхэлдээ:',S.Итгэл.value_counts().to_dict())
R['Акаунт_төрөл']=R.BC_код.map(atype)
out='/home/user/uag-report/Данс_BC_харилцагч_маплинг.xlsx'
cols=['file','k4','d','amt','cpn','cpname','desc','Акаунт_төрөл','BC_код','BC_нэр','Type','Дүрэм','Итгэл']
with pd.ExcelWriter(out) as w:
    S[cols].to_excel(w,sheet_name='Автомат_санал',index=False)
    bt.to_excel(w,sheet_name='Нарийвчлал',index=False)
    R.to_excel(w,sheet_name='Маплинг',index=False); SB.to_excel(w,sheet_name='Данс+утга',index=False); U.to_excel(w,sheet_name='Утгын_дүрэм',index=False)
    pd.DataFrame(sorted(own.items()),columns=['Өөрийн_данс','BC_Bank']).to_excel(w,sheet_name='Өөрийн_данс',index=False)
    S[S.Итгэл=='Шалгах'][cols].to_excel(w,sheet_name='Шалгах',index=False)
    M[['Түвшин','file','k4','d','amt','cpn','cpname','desc','Document No.','Bal. Account No.','Cust/Vend Name','Type']].to_excel(w,sheet_name='Тулгалт',index=False)
