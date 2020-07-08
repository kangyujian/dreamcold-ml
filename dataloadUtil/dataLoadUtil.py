import pandas as pd


def loadDataFromTxt(path,spli):
    res=[]
    with open(path,'r') as f:
        lines=f.readlines()
        for line in lines:
            tmp=line.split(spli)
            tmp=map(float,tmp)
            res.append(tmp)
    return res

def loadDataFromCsv(path):
    return pd.read_csv(path).values


def loadDataFromExcel(path,sheetName):
    return pd.read_excel(path,sheet_name=sheetName)
