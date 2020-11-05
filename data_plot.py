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

def scatter2D_background_2_plot_3version(data1,data2,plot_name_list,feature_x_name_list,feature_y_name_list,background_path_list):
    data1=np.array(data1)
    data2=np.array(data2)
    for i in range(3):
        background=plt.imread(background_path_list[i])
        plt.imshow(background)
        if i==0:
            plt.scatter(data2[:, 0], data2[:, 1], color="g", marker="x")
            plt.scatter(data1[:,0],data1[:,1],color="r",marker="o")

        elif i==1:
            plt.scatter(data2[:, 1], data2[:, 2], color="g", marker="x")
            plt.scatter(data1[:, 1], data1[:, 2], color="r", marker="o")

        else:
            plt.scatter(data2[:, 0], data2[:, 2], color="g", marker="x")
            plt.scatter(data1[:, 0], data1[:, 2], color="r", marker="o")

        plt.title(plot_name_list[i])
        plt.xlabel(feature_x_name_list[i])
        plt.ylabel(feature_y_name_list[i])
        plt.savefig("E:\\pythonBlack\\projection_neuron\\feature\\picture\\" + plot_name_list[i] + ".jpg")
        plt.show()

#data=[[i,i*0.5+i*i*0.1]for i in range(100)]
#data=np.array(data)
#scatter2D_background_plot(data,"pn","x","y","C:\\Users\\Black\\Desktop\\CellResource\\YZ-r.jpg")

from mpl_toolkits.mplot3d import Axes3D
def scatter3D_plot(data,plane=None):
    data=np.array(data)
    fig=plt.figure()
    ax=fig.add_subplot(111,projection='3d')
    for d in data:
        ax.scatter(d[0],d[1],d[2],s=20,c='r')
    if plane:
        x_max=np.max(data[:,0])
        x_min=np.min(data[:,0])
        y_max=np.max(data[:,1])
        y_min=np.min(data[:,1])
        x=np.arange(x_min,x_max,1)
        y=np.arange(y_min,y_max,1)
        X,Y=np.meshgrid(x,y)
        if plane[2]!=0:
            ax.plot_surface(X,Y,Z=(-plane[3]-plane[0]*X-plane[1]*Y)/plane[2],color='g',alpha=0.6)
        else:
            print("error plane!")
            return
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.view_init(elev=15,azim=10)
    plt.show()

def scatter3D_2_plot(data1,data2,plot_name):
    data1=np.array(data1)
    data2=np.array(data2)
    fig=plt.figure()
    ax=fig.add_subplot(111,projection='3d')
    for d1 in data1:
        ax.scatter(d1[0],d1[1],d1[2],s=20,c='r',marker='o')
    for d2 in data2:
        ax.scatter(d2[0],d2[1],d2[2],s=20,c='g',marker='x')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.view_init(elev=15, azim=10)
    plt.title(plot_name)
    plt.show()

def radio_shot_plot(center,tips,vision_flag=2,border=10):
    '''

    :param center: 中心点
    :param tips: 放射点，由中心点向此放射线
    :param vision_flag: 0,1,2标记为三个视角，YOZ，XOZ，XOY
    其中的颜色深浅由放射点的第三轴深度决定
    :return:
    '''
    center=np.array(center)
    tips=np.array(tips)
    #RGB 越浅则B越小、G越大；
    colors=['#80FF00','#80DF1F','#80BF3F','#809F5F','#807F7F','#805F9F','#803FBF','#801FDF','#8000FF']
    lower_limit=np.min(tips[:,vision_flag])
    distance=np.max(tips[:,vision_flag])-lower_limit
    step=distance/8
    if vision_flag==0:
        x_max=np.max(tips[:,1])
        x_min=np.min(tips[:,1])
        y_max=np.max(tips[:,2])
        y_min=np.min(tips[:,2])
        xlim=max(center[1]-x_min,x_max-center[1])
        ylim=max(center[2]-y_min,y_max-center[2])
        plt.xlim(center[1]-xlim-border,center[1]+xlim+border)
        plt.ylim(center[2]-ylim-border,center[2]+ylim+border)
        plt.xlabel("Y")
        plt.ylabel("Z")
    elif vision_flag==1:
        x_max=np.max(tips[:,0])
        x_min=np.min(tips[:,0])
        y_max=np.max(tips[:,2])
        y_min=np.min(tips[:,2])
        xlim = max(center[0] - x_min, x_max - center[0])
        ylim = max(center[2] - y_min, y_max - center[2])
        plt.xlim(center[0] - xlim-border, center[0] + xlim+border)
        plt.ylim(center[2] - ylim-border, center[2] + ylim+border)
        plt.xlabel("X")
        plt.ylabel("Z")
    else:
        x_max = np.max(tips[:, 0])
        x_min = np.min(tips[:, 0])
        y_max = np.max(tips[:, 1])
        y_min = np.min(tips[:, 1])
        xlim = max(center[0] - x_min, x_max - center[0])
        ylim = max(center[1] - y_min, y_max - center[1])
        plt.xlim(center[0] - xlim-border, center[0] + xlim+border)
        plt.ylim(center[1] - ylim-border, center[1] + ylim+border)
        plt.xlabel("X")
        plt.ylabel("Y")
    for i in range(len(tips)):
        color=colors[int((tips[i][vision_flag]-lower_limit)/step)]
        print(color)
        if vision_flag==0:
            mix0=[center[1],tips[i][1]]
            mix1=[center[2],tips[i][2]]
        elif vision_flag==1:
            mix0 = [center[0], tips[i][0]]
            mix1 = [center[2], tips[i][2]]
        else:
            mix0 = [center[0], tips[i][0]]
            mix1 = [center[1], tips[i][1]]
        plt.plot(mix0,mix1,color=color)
    plt.show()

def radar_plot(data,labels,plot_name):
    '''

    :param data: 多维度数据，可以有多个
    :param labels: 各个维度上的名称
    :return: 雷达图
    '''
    data=np.array(data)
    colors=['#80FF00','#0000FF','#80BF3F','#809F5F','#807F7F','#805F9F','#803FBF','#801FDF','#8000FF']
    if len(data[0])!=len(labels):
        print("Error!")
        return
    size=len(labels)
    fig=plt.figure()
    ax=fig.add_subplot(111,polar=True)
    angles=np.linspace(0,2*np.pi,size,endpoint=False)
    angles=np.concatenate((angles,[angles[0]]))#闭合
    for i,d in enumerate(data):
        b=np.concatenate((d,[d[0]]))#闭合
        ax.plot(angles,b,'bo-',linewidth=2)
        ax.fill(angles,b,facecolor=colors[i],alpha=0.25)
        ax.set_thetagrids(angles*180/np.pi,labels,fontproperties="SimHei")
        ax.set_title(plot_name,va='bottom',fontproperties="SimHei")
        ax.set_rlim(0,10)
        ax.grid(True)
    plt.show()
'''
labels=["length","bifur_name","mean_sum","std_sum","mean_std"]
data=[[0.8,3,4,1.7,7],[6,6,3.4,0.5,0.7]]
radar_plot(data,labels,"CP_17302_00005__236174_3429")
'''