import sys; sys.path.insert(0,'/tmp/claude-0/-home-claude/047d9ef0-79e1-503b-80bf-a6a9581215e6/scratchpad/xl')
from xlstyle import *
from load import D
import numpy as np, datetime as dt
from collections import defaultdict
OUT='/tmp/claude-0/-home-claude/047d9ef0-79e1-503b-80bf-a6a9581215e6/scratchpad/xl/out/'
import os; os.makedirs(OUT,exist_ok=True)
MON=['Oct','Nov','Dec','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep']
GAP={170,255,151,152,173}
LOG=open(OUT+'checks.txt','w')
def log(*a): print(*a); print(*a,file=LOG)

# ---------- Figure 2 ----------
R=D['Release']
pts=[(r[3],r[8]) for r in R[6:] if r[0] is not None and r[7]==1 and r[3] is not None and r[8] is not None]
log('Fig2 months used',len(pts))
tab=[(r[20],r[21]) for r in R[6:17]]
P=D['Params']
zones=P[45:52]
fig,(a1,a2)=plt.subplots(2,1,figsize=(W,12*CM),gridspec_kw=dict(hspace=0.62))
x,y=zip(*pts)
a1.scatter(x,y,s=7,color=BLUE,label='Recorded month, A3H030, 1987–2010',zorder=3,linewidths=0)
tx,ty=zip(*tab)
a1.plot(tx,ty,color=ORANGE,lw=1.8,label='Mean of each storage band (used)',zorder=4)
a1.set_xlim(0,7.2); a1.set_ylim(0,None)
a1.set_xlabel('Storage at the start of the month (Mm³)'); a1.set_ylabel('Release to the river\n(Ml/month)')
ax_style(a1); legend_bottom(a1,ncol=2,y=-0.30)
lab=['<7','7–14','14–21','21–35','35–57','57–85','≥85']
xi=np.arange(7); w=0.26
a2.bar(xi-w,[z[2] for z in zones],w,color=BLUE,label='Fit period (1966–74, 1981–86)')
a2.bar(xi,[z[3] for z in zones],w,color=ORANGE,label='Test period (1987–2009)')
a2.bar(xi+w,[z[7] for z in zones],w,color=GREY,label='Both periods, at most 1.00 (used)')
a2.set_xticks(xi,lab); a2.set_ylim(0,1.2)
a2.set_xlabel('Storage at the start of the month (% of full capacity)'); a2.set_ylabel('Share of registered\nvolume delivered')
ax_style(a2); legend_bottom(a2,ncol=3,y=-0.36)
fig.subplots_adjust(left=0.11,right=0.98,top=0.97,bottom=0.17)
save(fig,OUT+'Figure_2.png')
log('Fig2 zones fit',[round(z[2],3) for z in zones],'test',[round(z[3],3) for z in zones],'used',[round(z[7],3) for z in zones])

# ---------- Figure 3 ----------
cm=[P[21+i][6] for i in range(12)]
fig,ax=plt.subplots(figsize=(W,6.2*CM))
ax.bar(range(12),cm,0.55,color=BLUE)
ax.set_xticks(range(12),MON); ax.set_ylabel('Mean monthly volume (Mm³)'); ax.set_ylim(0,0.25)
ax_style(ax); fig.subplots_adjust(left=0.11,right=0.98,top=0.95,bottom=0.12)
save(fig,OUT+'Figure_3.png'); log('Fig3',[round(v,3) for v in cm])

# ---------- Figures 4 and 5: A3E003 ----------
d17=D['Data_17'][1:]
def hy(r): return r[2]
rain=defaultdict(dict); span=defaultdict(dict)
for r in d17:
    if r[0] is None: continue
    doubt=str(r[21] or '')
    if r[17] is not None and r[18] not in GAP and r[18] is not None and 'Rain' not in doubt:
        rain[r[2]][r[1]]=r[17]
    if r[19] is not None and r[20] not in GAP and r[20] is not None and 'Evap' not in doubt:
        span[r[2]][r[1]]=r[19]
d09=D['Data_09'][1:]
zr=defaultdict(float); zn=defaultdict(int)
for r in d09:
    if r[3] is None: continue
    zr[r[3]]+=r[7]; zn[r[3]]+=1
years=[y for y in range(1967,2009)]
st=[sum(rain[y].values()) if len(rain[y])==12 and y!=1975 else np.nan for y in years]
zz=[zr[y] if zn[y]==12 else np.nan for y in years]
log('Fig4 complete station years',sum(1 for v in st if v==v),[(y,round(v) if v==v else None) for y,v in zip(years,st)])
fig,ax=plt.subplots(figsize=(W,7*CM))
ax.bar(years,st,0.6,color=BLUE,label='Station A3E003 at the dam (complete years)')
ax.plot(years,zz,color=ORANGE,marker='o',ms=3.2,label='WR2012 rainfall zone A3B')
ax.set_xlim(1966,2009); ax.set_ylim(0,1200)
ax.set_xticks(range(1968,2009,4)); ax.set_xlabel('Hydrological year (October to September)')
ax.set_ylabel('Rainfall (mm per hydrological year)')
ax_style(ax); h,l=ax.get_legend_handles_labels(); legend_bottom(ax,h[::-1],l[::-1],ncol=2,y=-0.2)
fig.subplots_adjust(left=0.1,right=0.98,top=0.96,bottom=0.25)
save(fig,OUT+'Figure_4.png')

mo=[10,11,12,1,2,3,4,5,6,7,8,9]
rm=[np.mean([rain[y][m] for y in range(1967,2015) if m in rain[y]]) for m in mo]
sm=[np.mean([span[y][m] for y in range(1967,2015) if m in span[y]]) for m in mo]
log('Fig5 rain',[round(v,1) for v in rm],'span',[round(v,1) for v in sm],'Params S-pan',[P[21+i][2] for i in range(12)])
fig,ax=plt.subplots(figsize=(W,7*CM))
ax.bar(range(12),rm,0.55,color=BLUE,label='Rainfall')
sm=[P[21+i][2] for i in range(12)]
ax.plot(range(12),sm,color=ORANGE,marker='o',ms=3.5,label='S-pan evaporation')
ax.set_xticks(range(12),MON); ax.set_ylim(0,250); ax.set_ylabel('Mean monthly total (mm)')
ax_style(ax); h,l=ax.get_legend_handles_labels(); legend_bottom(ax,h[::-1],l[::-1],ncol=2,y=-0.13)
fig.subplots_adjust(left=0.1,right=0.98,top=0.96,bottom=0.2)
save(fig,OUT+'Figure_5.png')
