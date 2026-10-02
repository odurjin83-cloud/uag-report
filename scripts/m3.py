import pandas as pd,glob,re,os,warnings;warnings.filterwarnings('ignore')
L=pd.read_pickle('l.pkl'); L['k4']=L['Bank Account No.'].str[-4:]; K4=set(L.k4)
L['amt']=L.Amount.abs().round(2); L['amtl']=L['Amount (LCY)'].abs().round(2); L['d']=L['Posting Date'].dt.date
L=L[L.Amount<0].copy(); L['lid']=L['Entry No.']
def col(h,keys,excl=()):
    for i,c in enumerate(h):
        if any(k in c for k in keys) and not any(e in c for e in excl): return i
def num(v):
    try: return abs(float(str(v).replace(',','').replace(' ','')))
    except: return 0
def cpacc(v):
    m=re.search(r'MN\d{18}|\d{6,}',re.sub(r'\s','',str(v)) if str(v).startswith('MN') else str(v))
    if not m: return ''
    c=m.group(); return (c[-12:] if c.startswith('MN') else c).lstrip('0')
rows=[];bad=[]
for f in sorted(f for f in glob.glob('z/**/*',recursive=True) if os.path.isfile(f)):
    try: d=pd.read_excel(f,header=None,dtype=str)
    except Exception as e: bad.append((f,str(e)[:40]));continue
    top=' '.join(d.head(10).fillna('').astype(str).values.ravel())
    m=re.findall(r'\d{9,}',f.split('/')[-1]+' '+top)
    acc=next((x for x in m if x[-4:] in K4),None)
    if not acc: bad.append((f,'данс?'));continue
    if str(d.iat[0,0]).startswith('Хэвлэсэн'):   # ХХБ XLS
        st,cd,co,ca,cn,cs=1,0,3,5,5,7
    else:
        for i in range(min(40,len(d))):
            h=[str(v).lower().strip() for v in d.iloc[i].fillna('')]
            if col(h,['огноо','date']) is not None and col(h,['зарлага','дебит','debit','withdraw']) is not None: break
        else: bad.append((f,'толгой?'));continue
        st=i+1; cd=col(h,['огноо','date']); cs=col(h,['утга','description','тайлбар'])
        co=col(h,['зарлага','дебит','debit','withdraw'])
        ca=col(h,['харьцсан данс','харьцсан дансны дугаар','counter','хүлээн авагчийн данс','данс'],['үлдэгдэл','эзэмшигч','нэр'])
        cn=col(h,['харьцсан дансны нэр','нэр','name'],['банк'])
    for _,r in d.iloc[st:].iterrows():
        a=num(r.iloc[co]); dt=pd.to_datetime(str(r.iloc[cd])[:10],errors='coerce')
        if not a>0 or pd.isna(dt): continue
        rows.append(dict(file=f.split('/')[-1],k4=acc[-4:],d=dt.date(),amt=round(a,2),
          cpn=cpacc(r.iloc[ca]) if ca is not None else '',cpname=str(r.iloc[cn]) if cn is not None else '',
          desc=str(r.iloc[cs]) if cs is not None else ''))
S=pd.DataFrame(rows).drop_duplicates(subset=['k4','d','amt','cpn','desc']).reset_index(drop=True); S['sid']=S.index
used_s,used_l,pairs=set(),set(),[]
def run(tol,col_,lvl):
    c=S[~S.sid.isin(used_s)].merge(L[~L.lid.isin(used_l)][['lid','k4','d',col_]],left_on=['k4','amt'],right_on=['k4',col_])
    c['dd']=(pd.to_datetime(c.d_x)-pd.to_datetime(c.d_y)).dt.days.abs()
    for _,r in c[c.dd<=tol].sort_values('dd').iterrows():
        if r.sid in used_s or r.lid in used_l: continue
        used_s.add(r.sid);used_l.add(r.lid);pairs.append((r.sid,r.lid,lvl))
run(0,'amt','1-яг'); run(5,'amt','2-огноо±5'); run(5,'amtl','3-валют/LCY')
for tol in (0,3):
    G=L[~L.lid.isin(used_l)].groupby(['k4','d','Document No.']).agg(amt=('amt','sum'),lids=('lid',list)).reset_index(); G['amt']=G.amt.round(2)
    c=S[~S.sid.isin(used_s)].merge(G,on=['k4','amt'])
    c['dd']=(pd.to_datetime(c.d_x)-pd.to_datetime(c.d_y)).dt.days.abs()
    for _,r in c[c.dd<=tol].iterrows():
        if r.sid in used_s or any(i in used_l for i in r.lids): continue
        used_s.add(r.sid); [ (used_l.add(i),pairs.append((r.sid,i,'4-олон BC мөр'))) for i in r.lids]
P=pd.DataFrame(pairs,columns=['sid','lid','Түвшин'])
M=P.merge(S,on='sid').merge(L.drop(columns=['k4','d','amt']),on='lid')
US=S[~S.sid.isin(used_s)]; UL=L[~L.lid.isin(used_l)]
print('хуулга',len(S),'| тулгагдсан хуулга',len(used_s),f'({len(used_s)/len(S):.0%})','| BC',len(L),'тулгагдсан',len(used_l),f'({len(used_l)/len(L):.0%})')
print(P.Түвшин.value_counts().to_dict()); print('асуудалтай файл',len(bad)); [print(' ',b[0][-55:],b[1]) for b in bad]
print('тулгагдаагүй хуулга',US.k4.value_counts().head(10).to_dict()); print('тулгагдаагүй BC',UL.k4.value_counts().head(10).to_dict())
pd.to_pickle((S,L,M,US,UL),'r3.pkl')
# 5) олон хуулгын мөр = нэг BC мөр (цалин, тэтгэмж бөөнөөр)
S['grp']=S.desc.fillna('').str.upper().str.replace(r'[^А-ЯӨҮA-Z ]',' ',regex=True).str.split().str[:2].str.join(' ')
for key in (['k4','d'],['k4','d','grp']):
    U=S[~S.sid.isin(used_s)]
    G=U.groupby(key).agg(amt=('amt','sum'),sids=('sid',list),n=('sid','size')).reset_index(); G=G[G.n>1]; G['amt']=G.amt.round(2)
    c=G.merge(L[~L.lid.isin(used_l)][['lid','k4','d','amt']],on=['k4','d','amt'])
    for _,r in c.iterrows():
        if r.lid in used_l or any(s in used_s for s in r.sids): continue
        used_l.add(r.lid); [ (used_s.add(s),pairs.append((s,r.lid,'5-олон хуулгын мөр'))) for s in r.sids]
P=pd.DataFrame(pairs,columns=['sid','lid','Түвшин'])
M=P.merge(S,on='sid').merge(L.drop(columns=['k4','d','amt']),on='lid')
US=S[~S.sid.isin(used_s)]; UL=L[~L.lid.isin(used_l)]
print('ЭЦСИЙН: хуулга',f'{len(used_s)}/{len(S)} ({len(used_s)/len(S):.0%})','BC',f'{len(used_l)}/{len(L)} ({len(used_l)/len(L):.0%})',P.Түвшин.value_counts().to_dict())
pd.to_pickle((S,L,M,US,UL),'r3.pkl')
# --- Маплинг
M=M[M.cpn.str.len()>=6]
def summ(x):
    v=(x['Bal. Account No.'].fillna('').astype(str)+' | '+x['Cust/Vend Name'].fillna('').astype(str))
    vb=v.str.replace(r'-UTT\b','',regex=True)  # -UTT хувилбарыг нэг харилцагч гэж үзэх
    vc=v.value_counts(); vcb=vb.value_counts(); sh=vcb.iloc[0]/len(x)
    st='Тодорхой' if len(vcb)==1 else ('Давамгай' if sh>=0.8 and len(x)>=3 else 'Шалгах')
    return dict(Банкны_нэр=x.cpname.fillna('').mode().iat[0],BC_код=vcb.index[0].split(' | ')[0],BC_нэр=vcb.index[0].split(' | ')[1],
      UTT_хувилбартай='Тийм' if any('-UTT' in i for i in vc.index) else '',
      Type=x['Type'].fillna('').mode().iat[0],CashFlow=x['Cash Flow Code 2 Name'].fillna('').mode().iat[0],
      Хэлтэс=x['Department '].fillna('').mode().iat[0],ГҮ_тоо=len(x),Хувь=round(sh,2),Төлөв=st,
      Бусад='; '.join(f'{k} ({n})' for k,n in vcb.iloc[1:6].items()),Жишээ_утга=str(x.desc.iloc[0])[:90])
R=pd.DataFrame([{'Харьцсан_данс':k}|summ(x) for k,x in M.groupby('cpn')]).sort_values('ГҮ_тоо',ascending=False)
# Нэг данс олон зориулалт → утгаар ялгах дэд дүрэм
sub=[]
for k,x in M[M.cpn.isin(R[R.Төлөв=='Шалгах'].Харьцсан_данс)].groupby('cpn'):
    x=x.assign(g=x.desc.fillna('').str.upper().str.replace(r'[^А-ЯӨҮЁA-Z ]',' ',regex=True).str.split().apply(lambda w:' '.join([t for t in w if len(t)>3][:3])))
    for g,y in x.groupby('g'):
        vc=(y['Bal. Account No.'].fillna('').astype(str)+' | '+y['Type'].fillna('')).value_counts()
        sub.append(dict(Харьцсан_данс=k,Утгын_түлхүүр=g,ГҮ_тоо=len(y),BC_данс_Type=vc.index[0],Хувь=round(vc.iloc[0]/len(y),2),
          Төлөв='Тодорхой' if len(vc)==1 and len(y)>=2 else 'Шалгах',Жишээ=str(y.desc.iloc[0])[:90]))
SB=pd.DataFrame(sub)
import collections
S2=M.assign(t=M.desc.fillna('').str.lower().str.replace(r'[^a-zа-яөүё ]',' ',regex=True))
A=S.merge(L,on=['k4','d','amt']).assign(t=lambda z:z.desc.fillna('').str.lower().str.replace(r'[^a-zа-яөүё ]',' ',regex=True))
cnt=collections.Counter(w for t in A.t for w in set(t.split()) if len(w)>=4); rules=[]
for w,n in cnt.most_common(500):
    if n<5: break
    x=A[A.t.str.contains(rf'\b{w}\b')]; tv=x['Type'].fillna('?').value_counts(); tsh=tv.iloc[0]/len(x)
    if tsh<0.9: continue
    vc=(x['Bal. Account No.'].fillna('').astype(str)+' | '+x['Cust/Vend Name'].fillna('')).value_counts(); sh=vc.iloc[0]/len(x)
    rules.append(dict(Түлхүүр_үг=w,ГҮ_тоо=len(x),BC_Type=tv.index[0],Type_хувь=round(tsh,2),Эсрэг_данс=vc.index[0] if sh>=0.9 else '(дансаар ялгах)',
      Данс_хувь=round(sh,2),CashFlow=x['Cash Flow Code 2 Name'].fillna('').mode().iat[0],Жишээ=str(x.desc.iloc[0])[:90]))
U=pd.DataFrame(rules).sort_values('ГҮ_тоо',ascending=False)
out='/home/user/uag-report/Данс_BC_харилцагч_маплинг.xlsx'
with pd.ExcelWriter(out) as w:
    R.to_excel(w,sheet_name='Маплинг',index=False); SB.to_excel(w,sheet_name='Данс+утга',index=False)
    U.to_excel(w,sheet_name='Утгын_дүрэм',index=False); R[R.Төлөв!='Тодорхой'].to_excel(w,sheet_name='Шалгах',index=False)
    M[['Түвшин','file','k4','d','amt','cpn','cpname','desc','Document No.','Bal. Account No.','Cust/Vend Name','Type','Cash Flow Code 2 Name','Department ']].to_excel(w,sheet_name='Тулгалт',index=False)
    US.to_excel(w,sheet_name='Тулгагдаагүй_хуулга',index=False)
    UL[['Posting Date','Bank Account No.','Document No.','Description','Amount','Type','Bal. Account No.','Cust/Vend Name']].to_excel(w,sheet_name='Тулгагдаагүй_BC',index=False)
print(R.Төлөв.value_counts().to_dict(),'данс+утга',SB.Төлөв.value_counts().to_dict(),'утгын дүрэм',len(U))
print('Тулгагдаагүй хуулга төрлөөр', US.desc.fillna('').str.contains('Charges|шимтгэл',case=False).sum(),'нь шимтгэл')
