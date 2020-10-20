import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy

#heatmap + hierarchy_cluster

#df=pd.read_excel("C:\\Users\\Black\\Desktop\\ipy聚类分析\\dendrite_features_vaa3d1.xlsx",index_col=0)
#df=df.dropna(how="any")
#newdf=df[:100]
#print(newdf)
#clustermap(newdf.T,row_cluster=False,standard_scale=0)
#sns.heatmap(newdf.T)
#plt.show()

def hierarchy_cluster(data_cluster,method="single",labels=None,plt_name=None):
    z=hierarchy.linkage(data_cluster,method=method)
    #print(z)
    hierarchy.dendrogram(z,labels=labels)
    '''labels_cut=hierarchy.cut_tree(z,height=0.45)
    #print(labels_cut)
    dic={}
    for label_cut in labels_cut:
        if label_cut[0] not in dic:
            dic.update({label_cut[0]:1})
        else:
            dic[label_cut[0]]+=1
    print(dic)
    '''
    if plt_name:
        plt.title(plt_name)
    plt.show()
    return z

#print(newdf.index)
#hierarchy_cluster(newdf,newdf.index)

def heatmap(data_heatmap):
    sns.heatmap(data_heatmap.T)
    plt.show()

#heatmap(newdf)