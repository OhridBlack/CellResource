import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def violin_plot(data,features_name="curvature",labels=["1","2","3","4"]):
    fig,axes=plt.subplots(figsize=(12,5))
    axes.violinplot(data,showmeans=True,showmedians=True)
    axes.set_title(features_name)

    plt.setp(axes,xticks=[y+1 for y in range(len(data))],xticklabels=labels)
    plt.show()

#data=[np.random.normal(0,std,100)for std in range(6,10)]
#violin_plot(data)

def density2D_plot(feature_x,feature_y,plot_name,feature_x_name,feature_y_name):
    sns.kdeplot(feature_x,feature_y, shade=True)
    plt.title(plot_name)
    plt.xlabel(feature_x_name)
    plt.ylabel(feature_y_name)
    plt.show()

#mean, cov = [0, 2], [(1, .5), (.5, 1)]
#x, y = np.random.multivariate_normal(mean, cov, size=50).T
#density2D_plot(x,y,"plot_name","feature_x","feature_y")

def scatter2D_plot(data,plot_name,feature_x_name,feature_y_name):
    sns.lmplot(x=feature_x_name,y=feature_y_name,data=data,scatter=True)
    plt.title(plot_name)
    plt.show()

#data=[[5*i,i*i]for i in range(100)]
#data=np.array(data)
#scatter2D_plot(data,"plot_name","feature_x","feature_y")