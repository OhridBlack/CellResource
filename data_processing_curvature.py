from Curvature3D import count_curvature_features
from readSWC import readSWC_NT
from readSWC import NT
import pandas as pd
import os

def feature_csv_curvature(path,csv_name=None):
    '''

    :param path: 一个神经元类的文件夹，其中所有文件都是该类的神经元
    :param csv_name: 一个记录了 name length bifur_num curvature(mean_sum,std_sum,mean_std,std_std) 的excel文件
    mean_sum: 分支上所有点的曲率求和作为分支的曲率，各分支的曲率结果求均值
    std_sum:分支上所有点的曲率求和作为分支曲率，再对各分支的曲率结果求标准差
    mean_std:分支上所有点的曲率求标准差作为分支曲率，再对各分支的曲率结果求均值
    std_std:分支上所有点的曲率求标准差作为分支曲率，再对各分支的曲率结果求标准差
    :return:
    '''
    df=pd.DataFrame(columns={"name","length","bifur_num","mean_sum","std_sum","mean_std","std_std"})
    for file in os.listdir(path):
        total_path=path+"\\"+file
        nt=readSWC_NT(total_path)
        nt.count_length()
        length=nt.total_length
        mean_sum,std_sum,mean_std,std_std=count_curvature_features(nt)
        bifur_num=len(nt.branch_list)
        new={"name":file,
             "length":length,
             "bifur_num":bifur_num,
             "mean_sum":mean_sum,
             "std_sum":std_sum,
             "mean_std":mean_std,
             "std_std":std_std}
        df=df.append([new],ignore_index=True)
    df.to_csv(csv_name,columns=["name","length","bifur_num","mean_sum","std_sum","mean_std","std_std"])

#path_list=["MOs","MOp","VPM","CP","SSp\\SSp-bfd","SSp\\SSp-ul","SSp\\SSp-ll","SSp\\SSp-m","SSp\\SSp-n"]
#for path in path_list:
#    feature_csv_curvature("E:\\pythonBlack\\projection_neuron\\"+path,path+"_curvature_feature.csv")

def 
