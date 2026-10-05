"""Regenerate project plots from the transcribed CSV records; does not run FEA."""
from pathlib import Path
import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'Plots';OUT.mkdir(exist_ok=True)
def read(n):
    with (ROOT/'Results'/n).open() as f:return list(csv.DictReader(f))
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,'axes.spines.right':False,'figure.dpi':150,'savefig.dpi':200})
COLORS=['#286382','#ce7740']
def save(fig,name):
    fig.tight_layout();fig.savefig(OUT/(name+'.png'),bbox_inches='tight');fig.savefig(OUT/(name+'.svg'),bbox_inches='tight');plt.close(fig)
mass=read('mass.csv');fig,ax=plt.subplots(figsize=(7,4))
v=[float(r['mass_g']) for r in mass];bars=ax.bar([r['design'] for r in mass],v,color=COLORS,width=.5)
ax.bar_label(bars,labels=[f'{x:.2f} g' for x in v],padding=4);ax.set_ylim(0,700);ax.set_ylabel('Rocker mass (g)');ax.set_title('Mass reduction: 41.23 g (6.72%)');save(fig,'mass_comparison')
k=read('kinematics.csv');q=np.array([float(r['input_travel_mm']) for r in k]);s=np.array([float(r['damper_compression_mm']) for r in k])
fig,ax=plt.subplots(figsize=(8,4.6));ax.plot(q,s,'o-',color=COLORS[0],label='CAD measurements');ax.plot(q,.8*q,'--',color='#888888',label='Constant MR = 0.80 reference');ax.axhline(0,color='#cccccc',lw=.8);ax.axvline(0,color='#cccccc',lw=.8);ax.set_xlabel('Vertical surrogate input travel (mm): positive = bump');ax.set_ylabel('Damper compression (mm)');ax.set_title('Damper travel varies nonlinearly with input travel');ax.legend();ax.grid(alpha=.15);save(fig,'damper_travel')
fig,ax=plt.subplots(figsize=(8,4.6));mid=(q[1:]+q[:-1])/2;mr=np.diff(s)/np.diff(q);ax.plot(mid,mr,'o-',color=COLORS[0]);ax.axhline(.8,ls='--',color='#888888',label='Nominal ride target 0.80');ax.set_xlabel('Input interval midpoint (mm)');ax.set_ylabel('Interval-average motion ratio');ax.set_title('Decreasing motion ratio toward bump');ax.legend();ax.grid(alpha=.15);save(fig,'motion_ratio')
f=read('fea_results.csv');fig,axs=plt.subplots(1,2,figsize=(11,4.5))
for ax,key,ylabel in zip(axs,['max_nodal_von_mises_MPa','max_resultant_displacement_mm'],['Maximum nodal von Mises stress (MPa)','Maximum resultant displacement (mm)']):
    for j,d in enumerate(['Baseline','Optimized']):
        rows=[next(r for r in f if r['design']==d and r['load_case']==c and float(r['max_mesh_mm'])==1.5) for c in ['Bump +30 mm 6 kN','Reverse 2 kN']]
        values=[float(r[key]) for r in rows];b=ax.bar(np.arange(2)+(j-.5)*.3,values,width=.3,color=COLORS[j],label=d);ax.bar_label(b,labels=[f'{x:.2f}' if 'MPa' in key else f'{x:.5f}' for x in values],padding=3,fontsize=9)
    ax.set_xticks([0,1],['Bump +30 mm / 6 kN','Reverse / 2 kN']);ax.set_ylabel(ylabel);ax.set_ylim(0,ax.get_ylim()[1]*1.15);ax.legend(fontsize=9)
fig.suptitle('Matched 1.5 / 0.3 mm meshes: mass saving increases compliance');save(fig,'matched_mesh_comparison')
fig,axs=plt.subplots(1,2,figsize=(11,4.5))
for j,d in enumerate(['Baseline','Optimized']):
    rows=[r for r in f if r['design']==d and r['load_case']=='Bump +30 mm 6 kN'];x=[float(r['max_mesh_mm']) for r in rows]
    for ax,key in zip(axs,['max_nodal_von_mises_MPa','max_resultant_displacement_mm']):
        y=[float(r[key]) for r in rows];ax.plot(x,y,'o-',color=COLORS[j],label=d)
        for xx,yy in zip(x,y):ax.annotate(f'{yy:.2f}' if 'MPa' in key else f'{yy:.5f}',(xx,yy),xytext=(0,8),textcoords='offset points',ha='center',fontsize=9)
for ax,ylabel in zip(axs,['Maximum nodal von Mises stress (MPa)','Maximum resultant displacement (mm)']):
    ax.set_xlabel('Maximum mesh size (mm)');ax.set_xticks([1.5,1.2]);ax.invert_xaxis();ax.set_ylabel(ylabel);ax.margins(x=.25,y=.35);ax.legend(fontsize=9);ax.grid(alpha=.15)
fig.suptitle('Bump mesh refinement: stability over the final refinement interval');save(fig,'mesh_convergence')
fig,ax=plt.subplots(figsize=(7,5))
O=np.array([0.,0.]);A=np.array([-96.,0.]);B=np.array([28.73604009,76.8]);C=np.array([-232.81,-375.88]);D=np.array([328.74,76.8])
ax.plot([*A[:1],0,B[0]],[0,0,B[1]],'o-',color=COLORS[0],lw=3)
ax.plot([A[0],C[0]],[A[1],C[1]],color='#666666',lw=2,label='Pushrod');ax.plot([B[0],D[0]],[B[1],D[1]],color=COLORS[1],lw=4,label='Damper envelope')
for name,point in [('O: pivot',O),('A',A),('B',B),('C: guided input',C),('D: fixed mount',D)]:ax.annotate(name,point,xytext=(8,8),textcoords='offset points');ax.scatter(*point,color='#222222',s=25)
ax.set_xlabel('x (mm)');ax.set_ylabel('y (mm)');ax.set_aspect('equal');ax.set_title('Nominal ride hard points - planar mechanism');ax.grid(alpha=.15);ax.legend(loc='lower right');ax.margins(.15);save(fig,'mechanism_geometry')
print('Generated 6 charts in PNG and SVG formats.')
