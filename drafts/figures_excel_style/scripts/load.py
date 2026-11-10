import openpyxl,pickle,os
C='/tmp/claude-0/-home-claude/047d9ef0-79e1-503b-80bf-a6a9581215e6/scratchpad/xl/wb.pkl'
if not os.path.exists(C):
    wb=openpyxl.load_workbook('/home/claude/a31e-article-review/files/workbooks/A31E_Dam_Water_Balance_v2_caseM_FirmYield_sw1.xlsx',read_only=True,data_only=True)
    D={}
    for s in ['Graphs','Data_17','Data_25','Data_09','Data_34','Params','Release','Inputs','Sens']:
        D[s]=[list(r) for r in wb[s].iter_rows(values_only=True)]
    pickle.dump(D,open(C,'wb'))
D=pickle.load(open(C,'rb'))
