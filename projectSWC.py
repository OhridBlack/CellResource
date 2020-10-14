import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def show2D(data):
    plt.scatter(data[:,0],data[:,1],marker='o')
    plt.show()

def project2D(co_list,somaIdx,NeedShow=False):
    #投影到主平面上，并且以soma的坐标为原点平移
    pca=PCA()
    co_list=np.array(co_list)
    new_co_list=pca.fit_transform(co_list)
    new_co_list-=new_co_list[somaIdx]
    if NeedShow:
        show2D(new_co_list)
    return new_co_list

'''
from readSWC import readSWC_NT
nt=readSWC_NT("E:\\163data_resource\\5\\01_5.v3dpbd_smartTracing.swc")
co_list=nt.coordinate_list()
new_co_list=project2D(co_list,0,True)
'''