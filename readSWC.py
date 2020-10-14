import numpy as np

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

    def coordinate_list(self):
        co_list=[]
        for swc in self.swc_list:
            co_list.append([swc.x,swc.y,swc.z])
        return co_list

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

#swc_list=readNT("E:\\163data_resource\\5\\01_5.v3dpbd_smartTracing.swc")
#for swc in swc_list:
#    swc.show()
