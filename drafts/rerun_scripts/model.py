import pickle, bisect
d=pickle.load(open('/tmp/claude-0/-home-claude/047d9ef0-79e1-503b-80bf-a6a9581215e6/scratchpad/sw1.pkl','rb'))
I=d['inputs']; K,L,U,V=d['K'],d['L'],d['U'],d['V']
cap=7.07; low=0.166
def match(arr,x):  # MATCH type 1 (1-based)
    return bisect.bisect_right(arr,x)
def area(s):
    s=min(max(s,0),K[-1]); t=min(match(K,s),11)
    return L[t-1]+(s-K[t-1])*(L[t]-L[t-1])/(K[t]-K[t-1])
def rel(s):
    s=min(max(s,0),K[-1]); u=min(match(U,s),10)
    return (V[u-1]+(s-U[u-1])*(V[u]-V[u-1])/(U[u]-U[u-1]))/1000
def run(i0,i1,s0,inflow_x=1,evap_x=1,dem_x=1,demand=2.34,rule=3,pattern=1,series=1,canal_rec=False,release_x=1,lowu=low,rule_table=None):
    out=[]; s=s0
    rt=rule_table or d['rule']
    for i in range(i0,i1):
        r=I[i]; pos=r[4]
        a=area(s)
        q=(r[45] if series==1 else r[51])*inflow_x
        rain=r[30]*a/1e5
        ev=min(d['span'][pos-1]*d['pf'][pos-1]*evap_x*a/1e5, s+q+rain)
        rl=min(rel(s)*release_x, s+q+rain-ev)
        J=demand*dem_x*d['pat'][pos-1][pattern-1]/1.0  # pattern shares sum to 1
        z=match(d['zone'],s/cap*100)
        share=rt[z-1][rule-1]
        want = share*J if not canal_rec else (r[38] or 0)
        c=min(want, max(0,s+q+rain-ev-rl-lowu))
        m=s+q+rain-ev-rl-c; sp=max(0,m-cap); e=m-sp
        out.append(dict(date=r[0],hy=r[3],pos=pos,s=s,q=q,rain=rain,ev=ev,rl=rl,J=J,c=c,sp=sp,e=e,fail=1 if c<0.99*J else 0,srec=r[7],cvalid=r[14],crec=r[38]))
        s=e
    return out
