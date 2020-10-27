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
        self.total_branch_list=[]
        self.childrenDic={}

    def coordinate_list(self):
        co_list=[]
        for swc in self.swc_list:
            co_list.append([swc.x,swc.y,swc.z])
        return co_list

    def count_length(self):
        if self.total_length>0:
            return
        ans=0
        for swc in self.swc_list:
            if swc.pid!=-1:
                pswc=self.swc_list[swc.pid-1]
                ans+=math.sqrt((swc.x-pswc.x)**2+(swc.y-pswc.y)**2+(swc.z-pswc.z)**2)
        self.total_length=ans

    def count_tip_branch(self):
        if len(self.tip_list)>0 and len(self.branch_list)>0:
            return
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
        self.childrenDic=childrenDic
        maxSomaChildren=0
        for swc in self.start_list:
            if childrenDic[swc.id]>maxSomaChildren:
                self.soma=swc
                maxSomaChildren=childrenDic[swc.id]

    def count_total_branch(self):
        if len(self.total_branch_list)>0:
            return
        if len(self.tip_list)==0 or len(self.branch_list)==0:
            self.count_tip_branch()
        total_branch_list=[]
        for swc in self.tip_list:
            branch=[swc.id]
            pid=swc.pid
            while pid in self.childrenDic and self.childrenDic[pid]==1:
                branch.append(pid)
                pid=self.swc_list[pid-1].pid
            total_branch_list.append(branch)
        for swc in self.branch_list:
            branch=[swc.id]
            pid=swc.pid
            while pid in self.childrenDic and self.childrenDic[pid]==1:
                branch.append(pid)
                pid=self.swc_list[pid-1].pid
            total_branch_list.append(branch)
        self.total_branch_list=total_branch_list


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


#nt=readSWC_NT("E:\\163data_resource\\5\\01_5.v3dpbd_smartTracing.swc")
#nt=readSWC_NT("C:\\Users\\Black\\Desktop\\swc.txt")
#nt.count_total_branch()
#nt.count_length()
#print(nt.total_branch_list)
#print(nt.total_length)
#nt.count_tip_branch()
#print("tip numbers:",len(nt.tip_list))
#print("branch numbers:",len(nt.branch_list))
#print("start numbers:",len(nt.start_list))

