import numpy as np
import pandas as pd

def getNeuron(xlsx_path,type_name,feature_name):
    #type_name options: CP VPM MOp MOs SSp(-m,-bfd,-n,-ul,-ll)
    df=pd.read_excel(xlsx_path)
    boollist=[(each==type_name)for each in df[feature_name]]
    df_need=df[boollist]
    return df_need['name']

def writeTxt(writing_path,name_list):
    fp=open(writing_path,"w")
    for name in name_list:
        fp.write(name)
        fp.write("\n")
    fp.close()

#data=getNeuron("C:\\Users\\Black\\Desktop\\ipy聚类分析\\2800SEUJanelia_soma_region.xlsx","SSp-ll","registration")
#writeTxt("SSp-ll_NameList.txt",data)
