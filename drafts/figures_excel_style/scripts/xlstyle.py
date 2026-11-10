# Excel 2016-style chart look for matplotlib, with Arial-metric font (Liberation Sans)
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
for f in ['/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf',
          '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf']:
    fm.fontManager.addfont(f)

BLUE='#4472C4'; ORANGE='#ED7D31'; GREY='#A5A5A5'; GOLD='#FFC000'; LBLUE='#5B9BD5'; GREEN='#70AD47'
DARK='#264478'; TXT='#595959'; GRID='#D9D9D9'; AXIS='#BFBFBF'
CM=1/2.54
W=16*CM

plt.rcParams.update({
    'font.family':'Liberation Sans','font.size':8,'text.color':TXT,
    'axes.labelcolor':TXT,'axes.labelsize':8.5,'xtick.color':TXT,'ytick.color':TXT,
    'xtick.labelsize':8,'ytick.labelsize':8,'axes.edgecolor':AXIS,'axes.linewidth':0.75,
    'axes.grid':True,'axes.grid.axis':'y','grid.color':GRID,'grid.linewidth':0.75,
    'axes.axisbelow':True,'legend.frameon':False,'legend.fontsize':8,
    'lines.linewidth':1.6,'lines.markersize':4,'savefig.dpi':300,
    'axes.spines.top':False,'axes.spines.right':False,'axes.spines.left':False,
    'xtick.major.size':0,'ytick.major.size':0,'xtick.major.pad':4,'ytick.major.pad':4,
    'figure.facecolor':'white','axes.facecolor':'white','hatch.color':GREY,
})

def ax_style(ax, xgrid=False):
    ax.spines['bottom'].set_color(AXIS)
    ax.tick_params(axis='x',which='both',length=0)
    if xgrid: ax.grid(True,axis='x',color=GRID,linewidth=0.75)

def legend_bottom(ax_or_fig, handles=None, labels=None, ncol=4, y=-0.18, fig=False):
    kw=dict(loc='upper center',ncol=ncol,frameon=False,handlelength=2.2,columnspacing=1.6)
    if fig:
        return ax_or_fig.legend(handles,labels,bbox_to_anchor=(0.5,y),**kw)
    if handles is None:
        handles,labels=ax_or_fig.get_legend_handles_labels()
    return ax_or_fig.legend(handles,labels,bbox_to_anchor=(0.5,y),**kw)

def save(fig,path):
    # Excel chart area: white with a thin light-grey border
    fig.patches.append(matplotlib.patches.Rectangle((0.002,0.002),0.996,0.996,transform=fig.transFigure,
                       fill=False,edgecolor=GRID,linewidth=0.8,zorder=-1))
    fig.savefig(path,dpi=300,facecolor='white')
    plt.close(fig)
