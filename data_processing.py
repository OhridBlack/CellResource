from angle_hist import caculateAngle_Hist
from readSWC import NT,readSWC_NT
from other_features import other_features
import numpy as np
import pandas as pd
import os
from cluster_heatmap import hierarchy_cluster
from scipy.cluster import hierarchy

def feature_csv(path,csv_name=None):
    '''
    :param path: 一个神经元类的文件夹，其中所有文件都是该类的神经元
    :return:一个记录了 name area branch tip total(density) angle_hist(0-7) 的excel文件
    '''
    df=pd.DataFrame(columns={"name","area","branch density","tip density","total density",
                             "angle_hist 0","angle_hist 1","angle_hist 2","angle_hist 3",
                             "angle_hist 4","angle_hist 5","angle_hist 6","angle_hist 7"})
    for file in os.listdir(path):
        total_path=path+"\\"+file
        nt=readSWC_NT(total_path)
        nt.count_tip_branch()
        total_number=len(nt.swc_list)
        area, branch_density, tip_density, total_density,angle_hist=other_features(nt)
        new={"name":file,
                          "area":area,
                          "branch density":branch_density,
                          "tip density":tip_density,
                          "total density":total_density,
                          "angle_hist 0":angle_hist[0]/total_number,
                          "angle_hist 1":angle_hist[1]/total_number,
                          "angle_hist 2": angle_hist[2]/total_number,
                          "angle_hist 3": angle_hist[3]/total_number,
                          "angle_hist 4": angle_hist[4]/total_number,
                          "angle_hist 5": angle_hist[5]/total_number,
                          "angle_hist 6": angle_hist[6]/total_number,
                          "angle_hist 7": angle_hist[7]/total_number}
        #print(new)
        df=df.append([new],ignore_index=True)
    df.to_csv(csv_name,columns=["name","area","branch density","tip density","total density",
                             "angle_hist 0","angle_hist 1","angle_hist 2","angle_hist 3",
                             "angle_hist 4","angle_hist 5","angle_hist 6","angle_hist 7"])

#choose=["CP","MOs","MOp","VPM","SSp-bfd","SSp-ul","SSp-ll","SSp-m","SSp-n"]
#for chooseone in choose:
    #path="SSp\\"+chooseone if chooseone.startswith("SSp") else chooseone
    #feature_csv("E:\\pythonBlack\\projection_neuron\\"+path,chooseone+"_feature.csv")

def sort_label(labels,cluster_number,label_type):
    label_cluster=[[]for _ in range(cluster_number)]
    for i in range(len(label_type)):
        label_cluster[label_type[i][0]].append(labels[i])
    return label_cluster

def writeLabel(label_cluster,type):
    fp=open(type+"_cluster_label.txt","w")
    for i in range(len(label_cluster)):
        for label in label_cluster[i]:
            fp.write(label+" "+str(i)+"\n")
    fp.close()

def feature_hierarchy_cluster(type):
    '''

    :param type: 神经元类型名称
    :return: 一张层次聚类图，聚类完毕的结果
    '''
    df=pd.read_csv("feature\\"+type+"_feature.csv")
    #df=df[["name","angle_hist 0","angle_hist 1","angle_hist 2","angle_hist 3","angle_hist 4","angle_hist 5","angle_hist 6","angle_hist 7"]]
    labels=np.array(df["name"])
    values=np.array(df[["angle_hist 0","angle_hist 1","angle_hist 2","angle_hist 3","angle_hist 4","angle_hist 5","angle_hist 6","angle_hist 7"]])
    #print(labels)
    #print(values)
    z=hierarchy_cluster(values,"average",plt_name=type)
    return z,labels



#z,labels=feature_hierarchy_cluster("SSp")
'''
cp:0.45  2类
mop:0.45 3/4类
mos:0.5 4类
vpm:0.4 2类
ssp:0.32/0.31 3/4类
'''
#type_cut=hierarchy.cut_tree(z,height=0.32)
#label_cluster=sort_label(labels,10,type_cut)
#writeLabel(label_cluster,"SSp")
#print(label_cluster)

def neuronProjection(type_name,cluster_number):
    path_fixed="C:\\Users\\Black\\Desktop\\ipy聚类分析\\projection_matrix_allen_ml.xlsx"
    df=pd.read_excel(path_fixed,index_col=0)
    path_cluster_label="E:\\pythonBlack\\projection_neuron\\feature\\"+type_name+"_cluster_label.txt"
    fp=open(path_cluster_label,"r")
    content=fp.read().replace("r1_","")
    content=content.split()
    fp.close()
    name_list=[[]for _ in range(cluster_number)]
    for i in range(len(content)//2):
        type=int(content[2*i+1])
        name=content[2*i]
        if name.startswith("AA"):
            name=name.replace(".swc","")
        else:
            name=name.replace("."," ")
            name_l=name.split()
            name=name_l[0]
        name_list[type].append(name)
    df_list=[]
    for i in range(cluster_number):
        df_=pd.DataFrame()
        for name in name_list[i]:
            df_=df_.append(df.loc[name])
        df_list.append(df_)
    return df_list





neuronProjection("SSp",4)