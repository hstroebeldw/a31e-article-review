import openpyxl, pickle, sys
f=sys.argv[1]; out=sys.argv[2]
wb=openpyxl.load_workbook(f,data_only=True,read_only=True)
def col(ws,c,r0,r1): return [ws[f'{c}{r}'].value for r in range(r0,r1+1)]
d={}
ws=wb['Inputs']
rows=list(ws.iter_rows(min_row=1,max_row=894,values_only=True))
d['inputs_hdr']=rows[:6]
d['inputs']=rows[6:]
P=wb['Params']
d['span']=[P[f'C{r}'].value for r in range(22,34)]
d['pf']=[P[f'E{r}'].value for r in range(22,34)]
d['pat']=[(P[f'H{r}'].value,P[f'I{r}'].value) for r in range(22,34)]
d['zone']=[P[f'B{r}'].value for r in range(46,53)]
d['rule']=[[P.cell(r,c).value for c in range(6,10)] for r in range(46,53)]
d['p']={k:P[k].value for k in ['B4','B5','B6','B8','B9','B10','B11']}
C=wb['Curve']; d['K']=[C[f'K{r}'].value for r in range(5,17)]; d['L']=[C[f'L{r}'].value for r in range(5,17)]
R=wb['Release']; d['U']=[R[f'U{r}'].value for r in range(7,18)]; d['V']=[R[f'V{r}'].value for r in range(7,18)]
for n in ['Run_Ref','Run_Ref_N','Run_A','Run_A_N','Run_B','Run_B_N','Run_Test','Run_TestRec']:
    ws=wb[n]
    d[n]=list(ws.iter_rows(min_row=1,max_row=ws.max_row,values_only=True))
pickle.dump(d,open(out,'wb'))
