# model of r5.1 rev3 P rotation (3 slots, two copies per acknowledged save), incl. a restart between saves
def targets(meta,keep):
    c=sorted([s for s in 'ABC' if not meta[s]['bad'] and s!=keep], key=lambda s: meta[s]['seq'])
    return c[:2]
def load(files):
    meta={s:{'seq':-1,'bad':False} for s in 'ABC'}; ok=[]
    for s in 'ABC':
        f=files[s]
        if f=='torn': meta[s]['bad']=True
        elif f is not None: meta[s]['seq']=f['seq']; ok.append(s)
    if not ok: return meta,{'seq':0,'keep':''},set()
    best=max(ok,key=lambda s:files[s]['seq'])
    return meta,{'seq':max(files[s]['seq'] for s in ok),'keep':best},files[best]['rows']
def save(files,meta,st,rows,crash_at=None):
    t=targets(meta,st['keep']); seq=st['seq']+1; wrote=[]
    if not t: return False
    for i,s in enumerate(t):
        if crash_at==i: files[s]='torn'; return False
        files[s]={'seq':seq,'rows':set(rows)}; meta[s]['seq']=seq; wrote.append(s)
    st['seq']=seq; st['keep']=wrote[0]; return True
loss=0; cases=0
for N in range(1,40):
  for restart_every in [0,1,3]:
    for crash in [None,0,1]:
      for corrupt in [None,'A','B','C']:
        files={s:None for s in 'ABC'}; meta,st,_=load(files); acked=set(); rows=set()
        for n in range(1,N+1):
            if restart_every and n%restart_every==0: meta,st,rows=load(files); rows=set(rows)
            new=rows|{n}
            if save(files,meta,st,new,crash if n==N else None): rows=new; acked|={n}
            else: break
        if corrupt and files[corrupt] is not None: files[corrupt]='torn'
        _,_,rec=load(files); cases+=1
        if not acked<=rec: loss+=1; print('LOSS N',N,'restart',restart_every,'crash',crash,'corrupt',corrupt,'missing',sorted(acked-rec)[:5])
print('cases',cases,'cases losing an acknowledged row:',loss)
