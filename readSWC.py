import numpy as np
import math

class SWC:
    def __init__(self,id,type,x,y,z,radius,pid):
        self.id=id
        self.type=type
        self.x=x
        self.y=y
        self.z=z
        self.radius=radius
        self.pid=pid

    def show(self):
        print("SWC id:",self.id,"type:",self.type,"(x,y,z):(",self.x,self.y,self.z,") radius:",self.radius,"pid:",self.pid)

class NT:
    def __init__(self,swc_list):
        self.swc_list=swc_list
        self.tip_list=[]
        self.branch_list=[]
        self.start_list=[]
        self.soma=None
        self.total_length=0

    def coordinate_list(self):
        co_list=[]
        for swc in self.swc_list:
            co_list.append([swc.x,swc.y,swc.z])
        return co_list

    def count_length(self):
        ans=0
        for swc in self.swc_list:
            if swc.pid!=-1:
                pswc=self.swc_list[swc.pid-1]
                ans+=math.sqrt((swc.x-pswc.x)**2+(swc.y-pswc.y)**2+(swc.z-pswc.z)**2)
        self.total_length=ans

    def count_tip_branch(self):
        #get tip points and branch points
        childrenDic={}
        for swc in self.swc_list:
            if swc.pid==-1:
                self.start_list.append(swc)
            else:
                if swc.pid not in childrenDic:
                    childrenDic.update({swc.pid:1})
                else:
                    childrenDic[swc.pid]+=1

        for swc in self.swc_list:
            if swc.pid==-1:
                continue
            if swc.id not in childrenDic:
                self.tip_list.append(swc)
            elif childrenDic[swc.id]>=2:
                self.branch_list.append(swc)



    #def resample(self,step):


def readSWC(filepath):
    data=np.loadtxt(filepath,comments="#")
    swc_list=[]
    for d in data:
        swc_list.append(SWC(int(d[0]),int(d[1]),d[2],d[3],d[4],d[5],int(d[6])))
    return swc_list

def readSWC_NT(filepath):
    swc_list=readSWC(filepath)
    nt=NT(swc_list)
    return nt

#def readNTs(filepath):

#nt=readSWC_NT("E:\\163data_resource\\5\\01_5.v3dpbd_smartTracing.swc")
#nt.count_tip_branch()
#print("tip numbers:",len(nt.tip_list))
#print("branch numbers:",len(nt.branch_list))
#print("start numbers:",len(nt.start_list))

