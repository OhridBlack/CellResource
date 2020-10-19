from angle_hist import caculateAngle_Hist
from readSWC import NT,readSWC_NT
from other_features import other_features
import numpy as np
import pandas as pd
import os

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

choose=["CP","MOs","MOp","VPM","SSp-bfd","SSp-ul","SSp-ll","SSp-m","SSp-n"]
for chooseone in choose:
    path="SSp\\"+chooseone if chooseone.startswith("SSp") else chooseone
    feature_csv("E:\\pythonBlack\\projection_neuron\\"+path,chooseone+"_feature.csv")