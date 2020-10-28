import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def show2D(data,cut=None):
    plt.scatter(data[:,0],data[:,1],color="b",marker='o')
    plt.scatter(data[0,0],data[0,1],color="r",marker="x")
    if cut:
        x_max=np.max(data[:,0])
        x_min=np.min(data[:,0])
        x_limit=max(x_max,-x_min)
        x=np.linspace(-x_limit,x_limit,50)
        y=np.linspace(-x_limit,x_limit,50)
        y1=0*x
        y2=x
        y3=-x
        plt.plot(x,y1,color="black")
        plt.plot(x,y2,color="black")
        plt.plot(x,y3,color="black")
        x1=0*x
        plt.plot(x1,y,color="black")
    plt.show()

def project2D(co_list,somaIdx=0,NeedShow=False,needCut=None):
    #投影到主平面上，并且以soma的坐标为原点平移
    pca=PCA()
    co_list=np.array(co_list)
    new_co_list=pca.fit_transform(co_list)
    new_co_list-=new_co_list[somaIdx]
    if NeedShow:
        show2D(new_co_list,needCut)
    return new_co_list

'''
from readSWC import readSWC_NT,NT

nt=readSWC_NT("E:\\163data_resource\\5\\01_5.v3dpbd_smartTracing.swc")
co_list=nt.coordinate_list()
new_co_list=project2D(co_list,0,True)

nt=readSWC_NT("E:\\2710_r1\\r1_1708\\r1_17302_00005.semi_r.swc")
co_list=nt.coordinate_list()
new_co_list=project2D(co_list,0,True,True)
'''