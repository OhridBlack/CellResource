import os
import numpy as np
from readSWC import readSWC_NT,NT
from orientationXY import readArbor,Arbor
from data_plot import scatter3D_2_plot,scatter2D_background_2_plot_3version,radio_shot_plot

'''
for file in os.listdir("E:\\1523_r10_4to8optimal"):
    if file.endswith(".txt"):
        file_new=file.replace("."," ")
        file_part=file_new.split()
        file_name=file_part[0]
        #print(file_name)
        os.system("copy E:\\1523_r10_4to8optimal\\"+file+" E:\\pythonBlack\\projection_neuron\\arbor\\"+file_name+".txt")
'''

def findArborFile(cell_type,max_type_num):
    '''cell_type: SSp VPM MOp MOs CP'''
    arbor_file_set=set()
    for file in os.listdir("E:\\pythonBlack\\projection_neuron\\arbor"):
        arbor_file_set.add(file)

    fp=open("E:\\pythonBlack\\projection_neuron\\feature\\"+cell_type+"_cluster_label.txt","r")
    lines=fp.readlines()
    fp.close()
    arbor_existing=[[]for _ in range(max_type_num)]
    for line in lines:
        d=line.split()
        name=d[0]
        type=int(d[1])
        name=name.replace("r1","r10")
        name=name.replace(".semi_r.swc",".txt")
        name=name.replace(".auto_r.swc",".txt")
        if name in arbor_file_set:
            arbor_existing[type].append(name)
    return arbor_existing

'''
cell_type_list=["CP","SSp","VPM","MOp","MOs"]
for cell_type in cell_type_list:
    arbor_existing=findArborFile(cell_type,4)
    for i in range(4):
        print(cell_type,i,len(arbor_existing[i]))
'''
'''
有充足arbor信息的神经元类型的聚类
CP:0,1
SSp:0,2
VPM:0,1
MOp:1
MOs:0
'''
def arbor_soma_show3D(celltype,cluster_index_list=[0],swc_num=20):
    arbor_existing=findArborFile(celltype,4)
    for index in cluster_index_list:
        data_soma=[]
        data_arbor=[]
        for i in range(swc_num):
            arbor_list=readArbor("E:\\pythonBlack\\projection_neuron\\arbor\\"+arbor_existing[index][i])
            for arbor in arbor_list:
                data_arbor.append(arbor.coordinate)
            swc_name=arbor_existing[index][i].replace("r10","r1")
            swc_name=swc_name.replace(".txt",".semi_r.swc")
            nt=readSWC_NT(celltype+"\\"+swc_name)
            nt.count_tip_branch()
            data_soma.append([nt.soma.x,nt.soma.y,nt.soma.z])
        plot_name=celltype+"_cluster"+str(index)+"_soma_arbor"
        scatter3D_2_plot(data_soma,data_arbor,plot_name)

'''
arbor_soma_show("CP",[0,1])
arbor_soma_show("VPM",[0,1])
arbor_soma_show("MOs",[0])
'''

def arbor_soma_show2D(celltype,cluster_index_list=[0],swc_num=20,background_path_list=None):
    arbor_existing = findArborFile(celltype, 4)
    for index in cluster_index_list:
        data_soma = []
        data_arbor = []
        for i in range(swc_num):
            arbor_list = readArbor("E:\\pythonBlack\\projection_neuron\\arbor\\" + arbor_existing[index][i])
            for arbor in arbor_list:
                data_arbor.append(arbor.coordinate)
            swc_name = arbor_existing[index][i].replace("r10", "r1")
            swc_name = swc_name.replace(".txt", ".semi_r.swc")
            nt = readSWC_NT(celltype + "\\" + swc_name)
            nt.count_tip_branch()
            data_soma.append([nt.soma.x, nt.soma.y, nt.soma.z])
        plot_name = celltype + "_cluster" + str(index) + "_soma_arbor"
        #scatter3D_2_plot(data_soma, data_arbor, plot_name)
        scatter2D_background_2_plot_3version(data_soma,data_arbor,[plot_name+"_XoY",plot_name+"_YoZ",plot_name+"_XoZ"],
                                             ["x","y","x"],["y","z","z"],background_path_list)

'''
background_path_list=["C:\\Users\\Black\\Desktop\\CellResource\\XY-c.jpg",
                      "C:\\Users\\Black\\Desktop\\CellResource\\YZ.jpg",
                      "C:\\Users\\Black\\Desktop\\CellResource\\XZ.jpg"]
arbor_soma_show2D("CP",[0,1],20,background_path_list)
arbor_soma_show2D("VPM",[0],20,background_path_list)
arbor_soma_show2D("MOs",[0],20,background_path_list)
'''
