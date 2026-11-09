import sys; sys.path.insert(0,'/tmp/claude-0/-home-claude/047d9ef0-79e1-503b-80bf-a6a9581215e6/scratchpad/py')
from model import *
def stats(obs,sim):
    n=len(obs); mo=sum(obs)/n
    ss=sum((o-s)**2 for o,s in zip(obs,sim)); sd=sum((o-mo)**2 for o in obs)
    return dict(n=n,NSE=round(1-ss/sd,3),RSR=round((ss/sd)**.5,3),PBIAS=round(sum(o-s for o,s in zip(obs,sim))/sum(obs)*100,1))
def evaluate(out, years):
    m=[x for x in out if x['hy'] in years and x['cvalid']==1]
    mon=stats([x['crec'] for x in m],[x['c'] for x in m])
    yo=[];ys=[]
    for y in years:
        mm=[x for x in out if x['hy']==y]
        if len(mm)==12 and all(x['cvalid']==1 for x in mm):
            yo.append(sum(x['crec'] for x in mm)); ys.append(sum(x['c'] for x in mm))
    yr=stats(yo,ys)
    st=[x for x in out if x['hy'] in years and x['srec'] is not None]
    sto=stats([x['srec'] for x in st],[x['s'] for x in st])
    return mon,yr,sto
fy=list(range(1966,1975))+list(range(1981,1987))
idx=lambda y:(y-1936)*12
for rule in (2,3):
  for pat in (1,2):
    for series in (1,2):
        a=run(idx(1966),idx(1975),I[idx(1966)][7],rule=rule,pattern=pat,series=series)
        b=run(idx(1981),idx(1987),I[idx(1981)][7],rule=rule,pattern=pat,series=series)
        c=run(idx(1966),idx(1987),I[idx(1966)][7],rule=rule,pattern=pat,series=series)
        print('rule',rule,'pat',pat,'ser',series,'segments',evaluate(a+b,fy)[:2],' continuous',evaluate(c,fy)[:2])
# forward check
f=run(idx(1987),888,I[idx(1987)][7],rule=1,pattern=1)
print('forward',evaluate(f,list(range(1987,2010))))
f2=run(idx(1987),888,I[idx(1987)][7],rule=2,pattern=1)
print('forward rule2 (in-sample)',evaluate(f2,list(range(1987,2010)))[:2])
