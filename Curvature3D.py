#from LineCurvature2D import lineCurvature2D
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
    normal=normal/normal_length
    normal_l=np.array([0,0,1])
    theta=math.acos(np.dot(normal,normal_l))
    #theta=theta if theta>math.pi/2 else math.pi-theta
    axis=np.cross(normal,normal_l)
    R=rodrigues_rotation(axis,theta)
    a_new=np.dot(R,a.T)
    b_new=np.dot(R,b.T)
    c_new=np.dot(R,c.T)

    point_list_2d=[[a_new[0],a_new[1]],[b_new[0],b_new[1]],[c_new[0],c_new[1]]]
    return point_list_2d


