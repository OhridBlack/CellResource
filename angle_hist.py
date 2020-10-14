'''
树突分支的分布情况直方图特征
将三位神经元投影到主平面上，计算每条分支上的特征点与原点形成向量。较x轴正方向夹角的区间分布
每45度为一块，共分为8块区域
        2|1
         |
3        |       0
__________________
4        |       7
         |
        5|6
'''
import numpy as np
import matplotlib.pyplot as plt
import math

def showAngle_Hist(data):
    plt.hist(data,8,edgecolor='black')
    plt.xlabel('angle')
    plt.ylabel('numbers')
    plt.title('angle_hist')
    plt.show()

def caculateAngle_Hist(data,NeedShow=False):
    '''
    :param data:每个元素都是一个二维坐标
    :param NeedShow: 是否展示直方图
    0：【0.45），1：【45，90），2：【90，135），3：【135，180）
    4：(-135,-180】，5：（-90，-135】，6：（-45，-90】，7：（0，-45】
    :return:angle hist feature
    '''
    angle_hist=[0]*8
    theta_list=[]
    for p in data:
        theta=math.atan2(p[0],p[1])
        if theta<0:
            theta+=math.pi*2
        theta/=(math.pi/4)
        angle_hist[int(theta)]+=1
        theta_list.append(theta)
    if NeedShow:
        showAngle_Hist(theta_list)
    return angle_hist

'''
data=[
    [1,0],[1,0.2],
    [1,1],[1,1.2],
    [0,1],[-1,1.2],
    [-1,1],[-1,0.2],
    [-1,0],[-1,-0.2],
    [-1,-1],[-1,-1.2],
    [0,-1],[1,-1.2],
    [1,-1],[1,-0.2]
]
angle_hist=caculateAngle_Hist(data,True)
print(angle_hist)
'''