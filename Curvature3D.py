from LineCurvature2D import lineCurvature2D
from readSWC import NT
import math
import numpy as np
import random

def rodrigues_rotation(axis,radian):
    axis=np.array(axis)
    #print("axis",axis)
    #print("degree",radian/math.pi*180)
    length=math.sqrt(axis[0]**2+axis[1]**2+axis[2]**2)
    axis=axis/length

    cosTheta=math.cos(radian)
    sinTheata=math.sin(radian)

    matrix1=np.identity(3)*cosTheta
    #print("m1",matrix1)
    matrix2=(1-cosTheta)*np.array([[axis[0]*axis[0],axis[0]*axis[1],axis[0]*axis[2]],
                                   [axis[0]*axis[1],axis[1]*axis[1],axis[1]*axis[2]],
                                   [axis[0]*axis[2],axis[1]*axis[2],axis[2]*axis[2]]])
    #print("m2",matrix2)
    matrix3=sinTheata*np.array([[0,-axis[2],axis[1]],[axis[2],0,-axis[0]],[-axis[1],axis[0],0]])
    #print("m3",matrix3)

    R=matrix1+matrix2+matrix3
    #print("R",R)
    return R


def point3d_2d(a,b,c):
    '''

    :param a: point A
    :param b: point B 重要点
    :param c: point C
    :return:
    '''
    a=np.array(a)
    b=np.array(b)
    c=np.array(c)
    ba=a-b
    bc=c-b
    normal=np.cross(ba,bc)
    normal_length=math.sqrt(normal[0]**2+normal[1]**2+normal[2]**2)
    if normal_length==0:
        return [[0,0],[0,1],[0,2]]
    normal=normal/normal_length
    normal_l=np.array([0,0,1])
    theta=math.acos(np.dot(normal,normal_l))
    #theta=theta if theta>math.pi/2 else math.pi-theta
    if normal[0]==0 and normal[1]==0:
        a_new=a
        b_new=b
        c_new=c
    else:
        axis=np.cross(normal,normal_l)
        R=rodrigues_rotation(axis,theta)
        a_new=np.dot(R,a.T)
        b_new=np.dot(R,b.T)
        c_new=np.dot(R,c.T)

    point_list_2d=[[a_new[0],a_new[1]],[b_new[0],b_new[1]],[c_new[0],c_new[1]]]
    return point_list_2d

def curvature3d(a,b,c):
    lines=[[0,1],[1,2]]
    vertices2D=point3d_2d(a,b,c)
    k=lineCurvature2D(vertices2D,lines)
    return k[1]

def count_curvature_features(nt):
    if len(nt.total_branch_list)==0:
        nt.count_total_branch()
    invalid_branch_num=0
    total_branch_curvature_sum=[]
    total_branch_curvature_std=[]
    co_list=nt.coordinate_list()
    for branch in nt.total_branch_list:
        if len(branch)<3:
            invalid_branch_num+=1
            continue
        single_branch_curvature=[]
        for i in range(len(branch)-2):
            a=co_list[branch[i]-1]
            b=co_list[branch[i+1]-1]
            c=co_list[branch[i+2]-1]
            k=abs(curvature3d(a,b,c))
            single_branch_curvature.append(k)
        single_branch_curvature=np.array(single_branch_curvature)
        sum_curvature=np.sum(single_branch_curvature)
        std_curvature=np.std(single_branch_curvature)
        total_branch_curvature_sum.append(sum_curvature)
        total_branch_curvature_std.append(std_curvature)
    total_branch_curvature_std=np.array(total_branch_curvature_std)
    total_branch_curvature_sum=np.array(total_branch_curvature_sum)
    mean_sum=np.mean(total_branch_curvature_sum)
    std_sum=np.std(total_branch_curvature_sum)
    mean_std=np.mean(total_branch_curvature_std)
    std_std=np.std(total_branch_curvature_std)
    print("mean_sum",mean_sum)
    print("std_sum",std_sum)
    print("mean_std",mean_std)
    print("std_std",std_std)
    print("total "+str(invalid_branch_num)+" invalid branches!")
    return mean_sum,std_sum,mean_std,std_std

#from readSWC import readSWC_NT

#nt=readSWC_NT("E:\\pythonBlack\\projection_neuron\\MOs\\r1_AA0110.swc")
#count_curvature_features(nt)



