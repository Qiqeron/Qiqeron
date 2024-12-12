import pandas as pd

def chickenpox_by_sex():
    df=pd.read_csv('NISPUF17.csv')
    v=df[df['P_NUMVRC']>0] 
    men=v[v['SEX']==1]
    men=len(men[men['HAD_CPOX']==1])/len(men[men['HAD_CPOX']==2])
    dfw=v[v['SEX']==2]
    wen=len(dfw[dfw['HAD_CPOX']==1])/len(dfw[dfw['HAD_CPOX']==2])
    return({"men":men,"women":wen})

print(chickenpox_by_sex())