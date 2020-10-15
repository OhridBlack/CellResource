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

def hierarchy_cluster(data_cluster):
    z=hierarchy.linkage(data_cluster)
    hierarchy.dendrogram(z)
    plt.show()

#print(newdf.index)
#hierarchy_cluster(newdf)

def heatmap(data_heatmap):
    sns.heatmap(data_heatmap.T)
    plt.show()

#heatmap(newdf)