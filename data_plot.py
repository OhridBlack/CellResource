import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from skimage import transform
import skimage.data as d

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
    #sns.lmplot(x=feature_x_name,y=feature_y_name,data=data,scatter=True)
    data_plot=pd.DataFrame({feature_x_name:data[:,0],feature_y_name:data[:,1]})
    sns.scatterplot(x=feature_x_name,y=feature_y_name,data=data_plot)
    plt.title(plot_name)
    plt.show()

#data=[[5*i,i*i]for i in range(100)]
#data=np.array(data)
#scatter2D_plot(data,"plot_name","feature_x","feature_y")

def scatter_density_plot(data,plot_name,spec_feature,features_name):
    #data_plot=pd.DataFrame({features_name[0]:data[:,0],features_name[1]:data[:,1]})
    sns.pairplot(data, vars=features_name,
                 kind='scatter', diag_kind='kde',
                 hue=spec_feature, palette='husl')
    plt.title(plot_name)
    plt.show()

#iris=sns.load_dataset("iris")
#scatter_density_plot(iris,"iris","species",['sepal_width', 'sepal_length'])
#print(iris)

def scatter2D_background_plot(data,plot_name,feature_x_name,feature_y_name,background_path):
    background=plt.imread(background_path)
    #background=d.camera()
    data[:,0]=data[:,0]-np.min(data[:,0])
    data[:,1]=data[:,1]-np.min(data[:,1])
    dataX=np.max(data[:,0])
    dataY=np.max(data[:,1])
    print(dataX)
    print(dataY)
    #background_new=transform.resize(background,(int(dataY),int(dataX)))
    plt.imshow(background)
    #plt.imshow(background_new)
    plt.xlim(0,max(dataX,800))
    plt.ylim(0,max(dataY,600))
    plt.scatter(data[:,0],data[:,1])
    plt.title(plot_name)
    plt.xlabel(feature_x_name)
    plt.ylabel(feature_y_name)
    plt.show()

#data=[[i,i*0.5+i*i*0.1]for i in range(100)]
#data=np.array(data)
#scatter2D_background_plot(data,"pn","x","y","C:\\Users\\Black\\Desktop\\CellResource\\YZ-r.jpg")
