# model of r5.1 rev4 P store: 5 slots, ack only after two copies, commit marker; load = highest committed version
S='ABCDE'
def load(files,marker):
    meta={s:{'seq':-1,'bad':False} for s in S}; valid={}
    for s in S:
        f=files[s]
        if f is None: continue
        if f=='torn' or f.get('damaged'): meta[s]['bad']=True; continue
        meta[s]['seq']=f['seq']; valid[s]=f
    stat={}
    for s,f in valid.items(): stat.setdefault(f['seq'],[]).append(s)
    mk=marker['seq'] if marker and marker!='torn' else -1
    committed=[q for q,sl in stat.items() if len(sl)>=2 or q==mk]
    cs=max(committed) if committed else -1
    block = mk>cs
    if cs<0: return meta,{'seq':max([mk,0]+list(stat)),'keep':set()},set(),block,False
    sl=stat[cs]; split=len({frozenset(valid[s]['rows']) for s in sl})>1
    return meta,{'seq':max([mk,0]+list(stat)),'keep':set(sl)},set(valid[sl[0]]['rows']),block,split
def save(files,mark,meta,st,rows,fail=None,crash=None):
    c=sorted([s for s in S if not meta[s]['bad'] and s not in st['keep']],key=lambda s:meta[s]['seq'])
    if len(c)<2: return False
    t1,t2=c[0],c[1]; seq=st['seq']+1; st['seq']=seq
    if crash=='t1': files[t1]='torn'; raise SystemExit
    if fail=='t1': meta[t1]['bad']=True; return False
    files[t1]={'seq':seq,'rows':set(rows)}; meta[t1]['seq']=seq
    if crash=='t2': files[t2]='torn'; raise SystemExit
    if fail=='t2': meta[t2]['bad']=True; return False
    files[t2]={'seq':seq,'rows':set(rows)}; meta[t2]['seq']=seq
    if crash=='mark': mark['m']='torn'; raise SystemExit
    st['keep']={t1,t2}; mark['m']={'seq':seq}; return True
loss=0;cases=0;blocked=0
for N in range(1,30):
 for rst in [0,1,3]:
  for ev in [None,('crash','t1'),('crash','t2'),('crash','mark'),('fail','t1'),('fail','t2')]:
   for corrupt in [None]+list(S)+['marker']:
    files={s:None for s in S}; mark={'m':None}
    meta,st,rows,_,_=load(files,None); acked=set()
    try:
      for n in range(1,N+1):
        if rst and n%rst==0: meta,st,rows,_,_=load(files,mark['m']); rows=set(rows)
        new=rows|{n}; kw={}
        if n==N and ev: kw={ev[0]:ev[1]}
        if save(files,mark,meta,st,new,**kw): rows=new; acked.add(n)
        else: break
    except SystemExit: pass
    if corrupt=='marker': mark['m']='torn'
    elif corrupt and isinstance(files[corrupt],dict): files[corrupt]=dict(files[corrupt],damaged=True)
    _,_,rec,blk,split=load(files,mark['m']); cases+=1
    if blk or split: blocked+=1; continue      # safe stop: nothing overwritten, files kept for recovery
    if not acked<=rec: loss+=1; print('LOSS',N,rst,ev,corrupt,sorted(acked-rec)[:3])
print('cases',cases,'silent loss of an acknowledged row:',loss,'| safe stops (block):',blocked)
# reviewer counterexamples
f={s:None for s in S}; m={'m':None}; meta,st,rows,_,_=load(f,None)
for n in range(1,502):
    assert save(f,m,meta,st,set(range(1,n+1)))
f[sorted(st['keep'])[0]]=dict(f[sorted(st['keep'])[0]],damaged=True)
print('501 acked, one of its copies unreadable ->',max(load(f,m['m'])[2]))
f2={s:None for s in S}; m2={'m':None}; meta,st,rows,_,_=load(f2,None)
for n in range(1,501): save(f2,m2,meta,st,set(range(1,n+1)))
ok=save(f2,m2,meta,st,set(range(1,502)),fail='t2'); print('second copy rejected -> acknowledged?',ok,'| after restart max row:',max(load(f2,m2['m'])[2]))
k=sorted(st['keep']); f3={s:(dict(v) if isinstance(v,dict) else v) for s,v in f.items()}
# same Seq, both copies readable but different (A has 500 rows, B 501) -> must not silently pick one
f4={'A':{'seq':501,'rows':set(range(1,501))},'B':{'seq':501,'rows':set(range(1,502))},'C':None,'D':None,'E':None}
r=load(f4,{'seq':501}); print('same Seq, copies differ -> block/split:',r[3] or r[4])
