import numpy as np
from readSWC import NT
from readSWC import readSWC_NT
from projectSWC import project2D
from angle_hist import caculateAngle_Hist
'''
other features:
1、 area ：after projecting the 3d swc points to 2d, the area of region
2、 branch density: the number of branch points / area
3、 tip density: the number of tip points / area
4、 total density: the number of total points / area 
5、 follow x/y: the angle between the normal of projected plane and X-axis or Y-axis
'''

def area_angleHist(NT,somaIdx=0):
    co_list=NT.coordinate_list()
    co_list_projected=project2D(co_list,somaIdx)
    x_min=np.min(co_list_projected[:,0])
    x_max=np.max(co_list_projected[:,0])
    y_min = np.min(co_list_projected[:, 1])
    y_max = np.max(co_list_projected[:, 1])
    area=(x_max-x_min)*(y_max-y_min)
    angle_hist=caculateAngle_Hist(co_list_projected,True)

    return area,[[x_min,y_min],[x_max,y_max]],angle_hist

def other_features(NT):
    a,rect,angle_hist=area_angleHist(NT)
    branch_number=len(NT.branch_list)
    tip_number=len(NT.tip_list)
    total_number=len(NT.swc_list)
    branch_density=branch_number/a
    tip_density=tip_number/a
    total_density=total_number/a
    print("area:",a)
    print("rect:",rect)
    print("branch_density:",branch_density)
    print("tip_density:",tip_density)
    print("total_density:",total_density)
    print("angle_hist",angle_hist)
    return a,branch_density,tip_density,total_density,angle_hist

#nt=readSWC_NT("C:\\Users\\Black\\Desktop\\r10_with_autoarbor_m1\\r10_17302_00001.swc")
#nt.count_tip_branch()
#print("total numbers:",len(nt.swc_list))
#print("tip numbers:",len(nt.tip_list))
#print("branch numbers:",len(nt.branch_list))
#print("start numbers:",len(nt.start_list))
#other_features(nt)

#nt=readSWC_NT("E:\\pythonBlack\\projection_neuron\\SSp\\SSp-ul\\r1_17543_00140.semi_r.swc")
#nt.count_tip_branch()
#print(len(nt.start_list))
#area_angleHist(nt)