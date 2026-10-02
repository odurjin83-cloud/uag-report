import pandas as pd,glob,re,os,warnings;warnings.filterwarnings('ignore')
L=pd.read_pickle('/tmp/claude-0/s/l.pkl')
L['k4']=L['Bank Account No.'].str[-4:]; L['amt']=L['Amount'].abs().round(2); L['d']=L['Posting Date'].dt.date
def col(h,keys,excl=()):
    for i,c in enumerate(h):
        if any(k in c for k in keys) and not any(e in c for e in excl): return i
rows=[]
for f in sorted(f for f in glob.glob('/tmp/claude-0/s/z/**/*',recursive=True) if os.path.isfile(f)):
    try: d=pd.read_excel(f,header=None,dtype=str)
    except Exception: continue
    m=re.findall(r'\d{9,}',f.split('/')[-1]+' '+' '.join(d.head(10).fillna('').astype(str).values.ravel()))
    acc=next((x for x in m if len(x)>=9),None)
    for i in range(min(40,len(d))):
        h=[str(v).lower().strip() for v in d.iloc[i].fillna('')]
        if sum(any(k in c for k in ['огноо','date','утга','дебит','зарлага','debit','данс']) for c in h)>=3: break
    else: continue
    cd=col(h,['огноо','date']); cs=col(h,['утга','description','тайлбар'])
    co=col(h,['зарлага','дебит','debit','withdraw']); ca=col(h,['харьцсан данс','харьцсан дансны дугаар','counter','хүлээн авагчийн данс','данс'],['үлдэгдэл','эзэмшигч'])
    cn=col(h,['харьцсан дансны нэр','нэр','name'],['банк'])
    if None in (cd,co,ca) or acc is None: continue
    for _,r in d.iloc[i+1:].iterrows():
        try: a=abs(float(str(r.iloc[co]).replace(',','')))
        except: continue
        if a==0: continue
        dt=pd.to_datetime(str(r.iloc[cd])[:10],errors='coerce')
        if pd.isna(dt): continue
        cp=re.sub(r'\s','',str(r.iloc[ca])) if pd.notna(r.iloc[ca]) else ''
        rows.append(dict(k4=acc[-4:],d=dt.date(),amt=round(a,2),cp=cp,cpname=str(r.iloc[cn]) if cn is not None else '',desc=str(r.iloc[cs]) if cs is not None else ''))
S=pd.DataFrame(rows).drop_duplicates()
print('statement outflows',len(S))
M=S.merge(L,on=['k4','d','amt'],how='inner')
M=M[M.cp.str.match(r'^(MN)?\d{6,}$')]
M['cp']=M.cp.map(lambda c: c[-12:] if c.startswith('MN') else c).str.lstrip('0'); M=M[M.cp!='']  # IBAN→дансны дугаар
print('matched',len(M))
M.to_pickle('/tmp/claude-0/s/M.pkl')
print(len(M)); g=M.groupby('cp')
def summ(x):
    v=x['Bal. Account No.'].fillna('').astype(str)+' | '+x['Cust/Vend Name'].fillna('').astype(str)
    vc=v.fillna('?').value_counts(dropna=False)
    top=vc.index[0]; share=vc.iloc[0]/len(x)
    st='Тодорхой' if len(vc)==1 and len(x)>=1 else ('Давамгай' if share>=0.8 else 'Шалгах')
    return pd.Series(dict(Банкны_нэр=x.cpname.fillna('').mode().iat[0],BC_код=top.split(' | ')[0],BC_нэр=top.split(' | ')[1],
      Төрөл=x['Type'].fillna('').mode().iat[0],ГҮ_тоо=len(x),Хувь=round(share,2),Хувилбарууд=len(vc),Төлөв=st,
      Бусад='; '.join(f'{k} ({n})' for k,n in vc.iloc[1:6].items()),Жишээ_утга=x.desc.iloc[0][:80]))
R=pd.DataFrame([summ(x).rename(None).to_dict()|{'cp':k} for k,x in g if len(x)]).rename(columns={'cp':'Харьцсан_данс'}).sort_values('ГҮ_тоо',ascending=False)
out='/home/user/uag-report/Данс_BC_харилцагч_маплинг.xlsx'
with pd.ExcelWriter(out) as w:
    R.to_excel(w,sheet_name='Маплинг',index=False); R[R.Төлөв!='Тодорхой'].to_excel(w,sheet_name='Шалгах',index=False)
    M[['k4','d','amt','cp','cpname','desc','Document No.','Bal. Account No.','Cust/Vend Name','Type','Cash Flow Code 2','Department ']].to_excel(w,sheet_name='Тулгалт',index=False)
print(R.Төлөв.value_counts()); print(R.head(15).to_string(max_colwidth=30))
# --- Гүйлгээний утгын түлхүүр үг → BC
import collections
S2=S.merge(L,on=['k4','d','amt'])  # бүх тулгагдсан (данс байхгүй ч)
S2['t']=S2.desc.fillna('').str.lower().str.replace(r'[^a-zа-яөүё ]',' ',regex=True)
cnt=collections.Counter(w for t in S2.t for w in set(t.split()) if len(w)>=4)
rules=[]
for w,n in cnt.most_common(400):
    if n<5: break
    x=S2[S2.t.str.contains(rf'\b{w}\b')]
    v=x['Type'].fillna('?')+' | '+x['Bal. Account No.'].fillna('').astype(str)+' | '+x['Cust/Vend Name'].fillna('')
    vc=v.value_counts(); sh=vc.iloc[0]/len(x)
    tv=x['Type'].fillna('?').value_counts(); tsh=tv.iloc[0]/len(x)
    if tsh<0.9: continue
    rules.append(dict(Түлхүүр_үг=w,ГҮ_тоо=len(x),BC_Type=tv.index[0],Type_хувь=round(tsh,2),
        Эсрэг_данс_харилцагч=vc.index[0] if sh>=0.9 else '(олон — дансаар ялгах)',Данс_хувь=round(sh,2),
        CashFlow=x['Cash Flow Code 2 Name'].mode().iat[0] if x['Cash Flow Code 2 Name'].notna().any() else '',
        Жишээ=x.desc.iloc[0][:90]))
U=pd.DataFrame(rules).sort_values('ГҮ_тоо',ascending=False)
with pd.ExcelWriter(out,mode='a',engine='openpyxl') as w: U.to_excel(w,sheet_name='Утгын_дүрэм',index=False)
print(len(U)); print(U.head(40).to_string(max_colwidth=40))
