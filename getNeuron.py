import numpy as np
import pandas as pd
import os

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

def readNeuronNamelist(type_name):
    fp=open("neuron_types\\"+type_name+"_NameList.txt","r")
    name_list=fp.read().split()
    return name_list

def copy(name_list,rsc_path,dis_path):
    for name in name_list:
        if name[0]=='a' and name[1]=='a':
            name.replace("aa","AA")
        else:
            name+=".auto_r"
        name="r1_"+name+".swc"
        os.system("copy "+rsc_path+name+" "+dis_path)
        #if ".semi_r" in name:
            #name.replace(".semi_r",".auto_r")
        #print("copy " + rsc_path + name + " " + dis_path)



#name_list=readNeuronNamelist("CP")
#copy(name_list,"E:\\2710_r1\\r1_1708\\","E:\\pythonBlack\\projection_neuron\\CP")
#copy(name_list,"E:\\2710_r1\\r1_1002\\","E:\\pythonBlack\\projection_neuron\\CP")

def check(name_list,path):
    length=len(name_list)
    ans=0
    for file in os.listdir("E:\\pythonBlack\\projection_neuron\\"+path):
        ans+=1
    if(length==ans):
        print("OK")
    print(length,ans)

#name_List=readNeuronNamelist("SSp-n")
#check(name_List,"SSp\\SSp-n")