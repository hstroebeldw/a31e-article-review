import sys; sys.path.insert(0,'/tmp/claude-0/-home-claude/047d9ef0-79e1-503b-80bf-a6a9581215e6/scratchpad/xl')
from xlstyle import *
from load import D
import numpy as np, datetime as dt
from collections import defaultdict
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import matplotlib.dates as mdates
OUT='/tmp/claude-0/-home-claude/047d9ef0-79e1-503b-80bf-a6a9581215e6/scratchpad/xl/out/'
GAP={170,255,151,152,173}
LOG=open(OUT+'checks_b.txt','w')
def log(*a): print(*a); print(*a,file=LOG)
def L(c):
    n=0
    for ch in c: n=n*26+ord(ch)-64
    return n-1
def yearaxis(ax,a,b,step):
    ax.xaxis.set_major_locator(mdates.YearLocator(step)); ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.set_xlim(dt.date(a,1,1),dt.date(b,1,1))
which=sys.argv[1:] or ['6','7','8','9','10','11','13','14']

# ---------- Figure 6 ----------
if '6' in which:
    inp=[r for r in D['Inputs'][6:] if r[0] is not None]
    infl=defaultdict(float); notrec=defaultdict(int); nm=defaultdict(int)
    for r in inp:
        y=r[L('D')]; infl[y]+=r[L('AT')]; nm[y]+=1
        if r[L('AH')]!=1: notrec[y]+=1
    allyrs=sorted(infl)
    med=float(np.median([infl[y] for y in allyrs]))
    zr=defaultdict(float); zn=defaultdict(int)
    for r in D['Data_09'][1:]:
        if r[3] is None: continue
        zr[r[3]]+=r[7]; zn[r[3]]+=1
    mean=np.mean([zr[y] for y in range(1920,2010)])
    yrs=list(range(1981,2010))
    log('Fig6 median inflow',round(med,2),'mean rain',round(mean,1),'years',len(allyrs),
        'grey',[y for y in yrs if notrec[y]], 'inflow', [(y,round(infl[y],2)) for y in yrs])
    fig,(a1,a2)=plt.subplots(2,1,figsize=(W,12*CM),gridspec_kw=dict(hspace=0.55))
    a1.bar(yrs,[zr[y] for y in yrs],0.6,color=BLUE,label='Rainfall, zone A3B')
    a1.axhline(mean,color=TXT,ls='--',lw=1,label='Mean 1920–2009 (%.0f mm)'%mean)
    a1.set_ylabel('Rainfall, zone A3B\n(mm/a)'); a1.set_ylim(0,1000)
    a2.bar(yrs,[infl[y] for y in yrs],0.6,color=[GREY if notrec[y] else ORANGE for y in yrs])
    a2.axhline(med,color=TXT,ls='--',lw=1)
    a2.set_ylabel('Inflow to the dam\n(Mm³/a)'); a2.set_xlabel('Hydrological year (October to September)')
    for a in (a1,a2):
        a.set_xlim(1980.3,2009.7); a.set_xticks(range(1982,2010,2)); ax_style(a)
    h,l=a1.get_legend_handles_labels(); legend_bottom(a1,h[::-1],l[::-1],ncol=2,y=-0.17)
    h=[Patch(color=ORANGE),Patch(color=GREY),Line2D([],[],color=TXT,ls='--',lw=1)]
    legend_bottom(a2,h,['Inflow as recorded (series 1)','Year with months not taken from the dam record','Median 1936–2009 (%.2f Mm³/a)'%med],ncol=2,y=-0.32)
    fig.subplots_adjust(left=0.11,right=0.98,top=0.97,bottom=0.2)
    save(fig,OUT+'Figure_6.png')

# ---------- Figure 7 ----------
if '7' in which:
    d25=[r for r in D['Data_25'][1:] if r[1] is not None and str(r[0]).startswith('Klein Maricopoort')]
    ok=[r for r in d25 if r[21] is not None and r[7]!='M']
    log('Fig7 M-flagged months left out',sum(1 for r in d25 if r[7]=='M'))
    t=[dt.date(r[1],r[2],1) for r in ok]
    p=[r[21] for r in ok]
    log('Fig7 storage months',len(p),t[0],t[-1])
    d17=[r for r in D['Data_17'][1:] if r[0] is not None]
    cy=defaultdict(float); cn=defaultdict(int); bad=defaultdict(int)
    for r in d17:
        y=r[2]
        if y<1936 or y>2024: continue
        v,q=r[5],r[6]; doubt='KMP_canal' in str(r[21] or '')
        if v is not None: cy[y]+=v
        cn[y]+=1
        if v is None or q is None or q in GAP or doubt: bad[y]+=1
    yrs=list(range(1936,2025))
    good=[y for y in yrs if cn[y]==12 and bad[y]==0]
    log('Fig7 canal counted years',len(good),'not counted',[y for y in yrs if y not in good])
    fig,(a1,a2)=plt.subplots(2,1,figsize=(W,12*CM),gridspec_kw=dict(hspace=0.55))
    # break the line at missing months
    import pandas as pd
    s=pd.Series(p,index=pd.to_datetime(t)).asfreq('MS')
    a1.plot(s.index,s.values,color=BLUE,lw=1.1)
    a1.axvline(dt.date(1966,1,1),color=TXT,ls=':',lw=1); a1.text(dt.date(1966,10,1),103,'Dam raised (1966)',fontsize=7.5,va='bottom')
    a1.set_ylim(0,110); a1.set_yticks(range(0,101,20)); a1.set_ylabel('Storage\n(% of capacity)')
    yearaxis(a1,1935,2026,10)
    a1.set_xlim(dt.date(1935,7,1),dt.date(2025,10,1))
    a2.bar([dt.date(y,4,1) for y in yrs],[cy[y] for y in yrs],width=250,
           color=[BLUE if y in good else GREY for y in yrs])
    a2.axhline(2.34,color=TXT,ls='--',lw=1)
    a2.set_ylabel('Canal volume\n(Mm³/a)'); a2.set_xlabel('Hydrological year (October to September); upper panel by month')
    yearaxis(a2,1935,2026,10); a2.set_xlim(dt.date(1935,7,1),dt.date(2025,10,1))
    for a in (a1,a2): ax_style(a)
    h=[Patch(color=BLUE),Patch(color=GREY),Line2D([],[],color=TXT,ls='--',lw=1)]
    legend_bottom(a2,h,['Canal volume, complete year','Year not counted: a missing or gap-coded month, or doubtful','Registered volume (2.34 Mm³/a)'],ncol=2,y=-0.32)
    fig.subplots_adjust(left=0.11,right=0.98,top=0.96,bottom=0.2)
    save(fig,OUT+'Figure_7.png')

# ---------- Figure 8 ----------
if '8' in which:
    import pandas as pd
    rz=[(dt.date(r[5],r[4],1),r[7]) for r in D['Data_09'][1:] if r[3] is not None]
    rz=[x for x in rz if dt.date(1965,12,1)<=x[0]<=dt.date(1992,8,1)]
    wf=[(dt.date(r[0],r[1],1),(r[3] if r[4] not in GAP else np.nan)) for r in D['Data_34'][1:] if r[0] is not None]
    log('Fig8 rain months',len(rz),'flow months',len(wf),'gap months',sum(1 for x in wf if x[1]!=x[1]))
    fig,(a1,a2)=plt.subplots(2,1,figsize=(W,12*CM),gridspec_kw=dict(hspace=0.35))
    a1.bar([x[0] for x in rz],[x[1] for x in rz],width=25,color=BLUE)
    a1.set_ylabel('Rainfall, zone A3B\n(mm/month)'); a1.set_ylim(0,300)
    s=pd.Series([x[1] for x in wf],index=pd.to_datetime([x[0] for x in wf])).asfreq('MS')
    a2.plot(s.index,s.values,color=ORANGE,lw=1.1)
    a2.axvline(dt.date(1984,1,1),color=TXT,ls=':',lw=1); a2.text(dt.date(1984,4,1),1.3,'January 1984',fontsize=7.5)
    a2.set_ylabel('Wilgeboomspruit, A3H016\n(Mm³/month)'); a2.set_xlabel('Month'); a2.set_ylim(0,1.4)
    for a in (a1,a2):
        yearaxis(a,1965,1993,4); a.set_xlim(dt.date(1965,11,1),dt.date(1992,10,1)); ax_style(a)
    fig.subplots_adjust(left=0.13,right=0.98,top=0.97,bottom=0.1)
    save(fig,OUT+'Figure_8.png')

# ---------- Figure 9 ----------
if '9' in which:
    G=[r for r in D['Graphs'][5:]]
    ts=[(r[0],r[1],r[2]) for r in G if r[0] is not None]
    fy=[(r[4],r[5],r[6]) for r in G if r[4] is not None]
    # reverse test: rule fitted on 1987-2009, run over 1966-1974 and 1981-1986 (rev2.py, zonecap_date=True)
    import io,contextlib
    src=open('/tmp/claude-0/-home-claude/047d9ef0-79e1-503b-80bf-a6a9581215e6/scratchpad/rev2.py').read().split('for zc in')[0]
    with contextlib.redirect_stdout(io.StringIO()): exec(src)
    allo=[]
    for a,b in ((1966,1975),(1981,1987)):
        i0=idx(a); allo+=run2(i0,idx(b),inp[i0][col('H')],2,2,True)
    yv=defaultdict(lambda:[0,0.0,0.0])
    for x in allo:
        d=yv[x['yr']]; d[0]+=x['cv']; d[2]+=x['L']
        if x['cv']==1: d[1]+=x['cr']
    rv=[(y,d[1],d[2]) for y,d in sorted(yv.items()) if d[0]==12]
    ob=np.array([v[1] for v in rv]); sm=np.array([v[2] for v in rv])
    log('Fig9 reverse years',len(rv),'NSE',round(1-((ob-sm)**2).sum()/((ob-ob.mean())**2).sum(),2),'PBIAS',round((ob.sum()-sm.sum())/ob.sum()*100,1))
    fo=[v for v in fy if v[1] is not None]
    ob=np.array([v[1] for v in fo]); sm=np.array([v[2] for v in fo])
    log('Fig9 forward years',len(fo),'NSE',round(1-((ob-sm)**2).sum()/((ob-ob.mean())**2).sum(),2),'PBIAS',round((ob.sum()-sm.sum())/ob.sum()*100,1))
    fig,(a1,a2)=plt.subplots(2,1,figsize=(W,12.5*CM),gridspec_kw=dict(hspace=0.62))
    a1.plot([x[0] for x in ts],[x[1] for x in ts],color=BLUE,lw=1.4,label='Recorded')
    a1.plot([x[0] for x in ts],[x[2] for x in ts],color=ORANGE,lw=1.4,label='Simulated')
    a1.axhline(7.07,color=TXT,ls='--',lw=1,label='Full supply (7.07 Mm³)')
    a1.set_ylim(0,8); a1.set_ylabel('Storage at end of\nmonth (Mm³)')
    yearaxis(a1,1987,2011,4); a1.set_xlim(dt.date(1987,9,1),dt.date(2010,10,1))
    a1.set_xlabel('Month, forward test (hydrological years 1987–2009)')
    legend_bottom(a1,ncol=3,y=-0.38)
    yrs=[v[0] for v in rv]+[v[0] for v in fo]
    rec=[v[1] for v in rv]+[v[1] for v in fo]; sim=[v[2] for v in rv]+[v[2] for v in fo]
    xs=np.array(yrs)
    a2.axvspan(1965.5,1986.5,color='#F2F2F2',zorder=0); a2.axvspan(1986.5,2009.5,color='#FFFFFF',zorder=0)
    a2.bar(xs-0.2,rec,0.4,color=BLUE,label='Recorded (complete years)')
    a2.bar(xs+0.2,sim,0.4,color=ORANGE,label='Simulated')
    a2.axhline(2.34,color=TXT,ls='--',lw=1,label='Registered volume (2.34 Mm³/a)')
    a2.text(1976,3.85,'Reverse test',ha='center',fontsize=7.5); a2.text(1998,3.85,'Forward test',ha='center',fontsize=7.5)
    a2.set_xlim(1965.5,2009.5); a2.set_ylim(0,4.2); a2.set_xticks(range(1966,2010,4))
    a2.set_ylabel('Canal volume\n(Mm³/a)'); a2.set_xlabel('Hydrological year (October to September)')
    for a in (a1,a2): ax_style(a)
    h,l=a2.get_legend_handles_labels(); legend_bottom(a2,h[1:]+h[:1],l[1:]+l[:1],ncol=3,y=-0.38)
    fig.subplots_adjust(left=0.11,right=0.98,top=0.97,bottom=0.17)
    save(fig,OUT+'Figure_9.png')
    log('Fig9 years in lower panel',yrs)

# ---------- Figure 10 ----------
if '10' in which:
    G=D['Graphs'][5:]
    m=[(r[9],r[10],r[11],r[12]) for r in G if r[9] is not None]
    yv=[(r[14],r[15],r[16]) for r in G if r[14] is not None]
    fig,(a1,a2)=plt.subplots(2,1,figsize=(W,12.5*CM),gridspec_kw=dict(hspace=0.55))
    a1.axvspan(dt.date(1975,10,1),dt.date(1981,10,1),color='#EDEDED',zorder=0,label='Doubtful inflow, 1975–1980')
    a1.plot([x[0] for x in m],[x[1] for x in m],color=ORANGE,lw=1.1,label='With the restriction rule')
    a1.plot([x[0] for x in m],[x[2] for x in m],color=BLUE,lw=1.1,label='Without restriction')
    a1.set_ylim(0,8); a1.set_ylabel('Storage at end of\nmonth (Mm³)')
    yearaxis(a1,1936,2011,10); a1.set_xlim(dt.date(1936,6,1),dt.date(2010,12,1))
    h,l=a1.get_legend_handles_labels(); legend_bottom(a1,h[1:]+h[:1],l[1:]+l[:1],ncol=3,y=-0.17)
    a2.axvspan(1975.5,1980.5,color='#EDEDED',zorder=0)
    a2.plot([x[0] for x in yv],[x[1] for x in yv],color=ORANGE,marker='o',ms=2.8,lw=1.3,label='With the restriction rule')
    a2.plot([x[0] for x in yv],[x[2] for x in yv],color=BLUE,marker='o',ms=2.8,lw=1.3,label='Without restriction')
    a2.axhline(2.34,color=TXT,ls='--',lw=1,label='Registered volume (2.34 Mm³/a)')
    a2.set_xlim(1935.5,2010); a2.set_ylim(0,2.6); a2.set_xticks(range(1940,2011,10))
    a2.set_ylabel('Canal delivery\n(Mm³/a)'); a2.set_xlabel('Hydrological year (October to September); upper panel by month')
    legend_bottom(a2,ncol=3,y=-0.36)
    for a in (a1,a2): ax_style(a)
    fig.subplots_adjust(left=0.11,right=0.98,top=0.97,bottom=0.16)
    save(fig,OUT+'Figure_10.png')
    log('Fig10 months',len(m),'years',len(yv))

# ---------- Figure 11 ----------
if '11' in which:
    S=D['Sens']
    rows=[r for r in S if isinstance(r[0],int)]
    rule=[(r[2],r[11],r[12]) for r in rows if 1<=r[0]<=11]
    none=[(r[2],r[11],r[12]) for r in rows if 27<=r[0]<=37]
    log('Fig11 rule',[(a,round(b,3),round(c,3)) for a,b,c in rule]); log('Fig11 none',[(a,round(b,3),round(c,3)) for a,b,c in none])
    fig,ax=plt.subplots(figsize=(W,8.5*CM))
    d=[x[0] for x in rule]
    ax.plot(d,[x[1] for x in none],color=BLUE,marker='o',ms=3.5,label='Without restriction: by time')
    ax.plot(d,[x[2] for x in none],color=BLUE,marker='o',ms=3.5,ls='--',label='Without restriction: by volume')
    ax.plot(d,[x[1] for x in rule],color=ORANGE,marker='o',ms=3.5,label='With the rule: by time')
    ax.plot(d,[x[2] for x in rule],color=ORANGE,marker='o',ms=3.5,ls='--',label='With the rule: by volume')
    for xv,t in ((2.34,'Registered\n2.34'),(2.73,'WR2012\n2.73')):
        ax.axvline(xv,color=TXT,ls=':',lw=1); ax.text(xv-0.03,0.42,t,ha='right',fontsize=7.5)
    ax.set_xlim(0.4,3.1); ax.set_ylim(0.4,1.0)
    ax.set_xlabel('Demand on the canal (Mm³/a)'); ax.set_ylabel('Reliability (74 years)')
    ax_style(ax); legend_bottom(ax,ncol=2,y=-0.2)
    fig.subplots_adjust(left=0.1,right=0.98,top=0.96,bottom=0.3)
    save(fig,OUT+'Figure_11.png')

# ---------- Figure 13 (values of 49b_Groundwater_results.txt, section 6.1) ----------
if '13' in which:
    S_=[(0.25,0.96,88.7+0.4),(0.50,2.30,88.8+0.4),(1.00,7.43,86.7+0.9),(2.34,40.83,74.6+3.9)]
    D_=[(0.25,4.92,0.3,None),(0.50,20.57,0.5,None),(1.00,117.5,1.0,2554),(2.00,160.2,1.5,3228),(2.34,164.0,1.5,3367)]
    fig,(a1,a2)=plt.subplots(2,1,figsize=(W,12.5*CM),gridspec_kw=dict(hspace=0.3))
    for a in (a1,a2):
        a.axvspan(0.27,0.70,color='#EDEDED',zorder=0); a.axvspan(1.80,2.05,color='#EDEDED',zorder=0)
        a.axvline(2.34,color=TXT,ls=':',lw=1)
    a1.plot([x[0] for x in S_],[x[1] for x in S_],color=BLUE,marker='o',ms=4,label='Structure S (outflow at 1 m)')
    a1.plot([x[0] for x in D_],[x[1] for x in D_],color=ORANGE,marker='o',ms=4,label='Structure D (outflow at 15.27 m)')
    nd=[x for x in D_ if x[3]]
    a1.scatter([x[0] for x in nd],[x[1] for x in nd],s=46,facecolors='white',edgecolors=ORANGE,linewidths=1.3,zorder=5,
               label='D: rate not delivered in full (label: Mm³/a delivered)')
    for x in nd: a1.text(x[0],x[1]*1.35,'%.2f'%(x[3]*365.25/1e6),ha='center',fontsize=7,color=ORANGE)
    a1.set_yscale('log'); a1.set_ylim(0.5,400); a1.set_yticks([0.5,1,2,5,10,20,50,100,200]); a1.set_yticklabels(['0.5','1','2','5','10','20','50','100','200'])
    a1.minorticks_off(); a1.set_ylabel('Mean drawdown in the\npumped cells (m)')
    a1.text(0.485,0.6,'Mean shortfall,\nReference, M and D',ha='center',fontsize=7); a1.text(1.925,0.6,'Longest\nevent',ha='center',fontsize=7)
    a1.text(2.36,0.6,'Registered\nvolume',ha='left',fontsize=7)
    a2.plot([x[0] for x in S_],[x[2] for x in S_],color=BLUE,marker='o',ms=4)
    a2.plot([x[0] for x in D_],[x[2] for x in D_],color=ORANGE,marker='o',ms=4)
    a2.scatter([x[0] for x in nd],[x[2] for x in nd],s=46,facecolors='white',edgecolors=ORANGE,linewidths=1.3,zorder=5)
    a2.set_ylim(0,100); a2.set_ylabel('Share taken from the\nrivers and streams (%)')
    a2.set_xlabel('Abstraction under the irrigated land (Mm³/a, entered)')
    for a in (a1,a2): a.set_xlim(0,2.6); ax_style(a)
    h,l=a1.get_legend_handles_labels(); fig.legend(h,l,loc='upper center',ncol=2,bbox_to_anchor=(0.5,0.075),frameon=False)
    fig.subplots_adjust(left=0.12,right=0.97,top=0.97,bottom=0.18)
    save(fig,OUT+'Figure_13.png')

# ---------- Figure 14 ----------
if '14' in which:
    G=D['Graphs'][5:]
    r=[x[30:37] for x in G if x[30] is not None]
    lv=[x[0] for x in r]
    log('Fig14 levels',len(lv),lv[:3],lv[-3:])
    fig,axs=plt.subplots(1,2,figsize=(W,8*CM),sharey=True,gridspec_kw=dict(wspace=0.1))
    for k,(a,t) in enumerate(zip(axs,['With the restriction rule','Without restriction'])):
        a.plot([x[1+k]*100 for x in r],lv,color='black',ls='--',lw=1.5,label='Reference')
        a.plot([x[3+k]*100 for x in r],lv,color=BLUE,lw=1.5,label='M: projected median, about 2050')
        a.plot([x[5+k]*100 for x in r],lv,color=ORANGE,lw=1.5,label='D: dry end of the projections, about 2050')
        a.set_title(t,fontsize=8.5,color=TXT,loc='left'); a.set_xlim(0,100); a.set_ylim(0,7.3)
        a.set_xlabel('Months with storage at or above the level (%)'); ax_style(a,xgrid=True)
    axs[0].set_ylabel('Storage (Mm³)')
    h,l=axs[0].get_legend_handles_labels(); fig.legend(h,l,loc='upper center',ncol=3,bbox_to_anchor=(0.5,0.1),frameon=False)
    fig.subplots_adjust(left=0.08,right=0.98,top=0.92,bottom=0.3)
    save(fig,OUT+'Figure_14.png')
