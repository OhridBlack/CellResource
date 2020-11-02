import numpy as np
import pandas as pd
import math
from readSWC import NT,readSWC_NT
from data_plot import scatter3D_plot,radio_shot_plot

def cluster2plane(data):
    '''
    按照三维点集（arbor cluster)拟合一个三维空间中的平面
    :param data: 三维点集
    :return: AX+BY+CZ+D=0 返回A,B,C,D四个值
    由于拟合最接近的平面，就是计算所有点到该平面的距离和最小，认为该点会通过离散点集的平均值
    '''
    data=np.array(data)
    mean_point=np.mean(data,axis=0)
    data_normal=data-mean_point
    w=np.dot(data_normal.T,data_normal)
    u,s,v=np.linalg.svd(w)
    a=v[2][0]
    b=v[2][1]
    c=v[2][2]
    d=-(a*mean_point[0]+b*mean_point[1]+c*mean_point[2])
    return a,b,c,d

def plane_X_Y_angle(a,b):
    '''

    :param a: 平面法向量（a,b,c),已经单位化了
    :param b:
    :param c:
    :return: 与X,Y轴的夹角
    '''
    angle_x=math.asin(a)
    angle_y=math.asin(b)
    if angle_x>math.pi/2:
        angle_x=math.pi-angle_x
    if angle_y>math.pi/2:
        angle_y=math.pi-angle_y
    angle_x/=math.pi
    angle_x*=180
    angle_y/=math.pi
    angle_y*=180
    return abs(angle_x),abs(angle_y)

class Arbor:
    def __init__(self,index,node_count,x,y,z):
        self.index=index
        self.node_count=node_count
        self.coordinate=[x,y,z]
    def show(self):
        print("index:",self.index)
        print("node_count:",self.node_count)
        print("coordinate:",self.coordinate)

def readArbor(path):
    fp=open(path,"r")
    content=fp.read().split()
    length=len(content)
    data=[]
    for i in range(5,length,5):
        arbor=Arbor(index=int(content[i]),node_count=int(content[i+1]),x=float(content[i+2]),y=float(content[i+3]),z=float(content[i+4]))
        arbor.show()
        data.append(arbor)
    fp.close()
    return data

def length_arbor_swc(swc,arbor):
    return math.sqrt((swc.x-arbor.coordinate[0])**2+(swc.y-arbor.coordinate[1])**2+(swc.z-arbor.coordinate[2])**2)

def swc_cluster_arbor(arbor_data,nt):
    length=len(arbor_data)
    cluster_swc_list=[[]for _ in range(length)]
    for swc in nt.swc_list:
        index=0
        distance=10e10
        for arbor in arbor_data:
            tmp=length_arbor_swc(swc,arbor)
            if tmp<distance:
                distance=tmp
                index=arbor.index
        cluster_swc_list[index-1].append(swc)
    return cluster_swc_list

'''
nt=readSWC_NT("E:\\1523_r10_4to8optimal\\r10_17302_00050.semi_r.swc")
data=readArbor("E:\\1523_r10_4to8optimal\\r10_17302_00050.semi_r.swc.autoarbor_m3.arborstat.txt")
cluster_swc_list=swc_cluster_arbor(data,nt)
data_swc=[]
for c in cluster_swc_list:
    data_swc=[]
    for swc in c:
        data_swc.append([swc.x,swc.y,swc.z])
    _a,_b,_c,_d=cluster2plane(data_swc)
    angle_x,angle_y=plane_X_Y_angle(_a,_b)
    print(angle_x,angle_y)
    #scatter3D_plot(data_swc,[a,b,c,d])
'''

'''
nt=readSWC_NT("E:\\1523_r10_4to8optimal\\r10_17302_00050.semi_r.swc")
data=readArbor("E:\\1523_r10_4to8optimal\\r10_17302_00050.semi_r.swc.autoarbor_m3.arborstat.txt")
cluster_swc_list=swc_cluster_arbor(data,nt)
for i,c in enumerate(cluster_swc_list):
    if i not in [0,2,7]:
        continue
    c_coordinate=[]
    for ci in c:
        c_coordinate.append([ci.x,ci.y,ci.z])
    radio_shot_plot(data[i].coordinate,c_coordinate,vision_flag=0,border=5)
    radio_shot_plot(data[i].coordinate, c_coordinate, vision_flag=1,border=5)
    radio_shot_plot(data[i].coordinate, c_coordinate, vision_flag=2,border=5)
'''


