import numpy as np
import math
def length(a,b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

def inv3(m):
    adjm=np.zeros((3,3))
    adjm[0][0]=m[1][1]*m[2][2]-m[2][1]*m[1][2]
    adjm[0][1]=-(m[1][0]*m[2][2]-m[2][0]*m[1][2])
    adjm[0][2]=m[1][0]*m[2][1]-m[2][0]*m[1][1]
    adjm[1][0]=-(m[0][1]*m[2][2]-m[2][1]*m[0][2])
    adjm[1][1]=m[0][0]*m[2][2]-m[2][0]*m[0][2]
    adjm[1][2]=-(m[0][0]*m[2][1]-m[2][0]*m[0][1])
    adjm[2][0]=m[0][2]*m[1][2]-m[1][1]*m[0][2]
    adjm[2][1]=-(m[0][1]*m[1][2]-m[1][0]*m[0][2])
    adjm[2][2]=m[0][0]*m[1][1]-m[1][0]*m[0][1]
    defm=m[0][0]*m[1][1]*m[2][2]-m[0][0]*m[2][1]*m[1][2]-m[1][0]*m[0][1]*m[2][2]+m[1][0]*m[2][1]*m[0][2]+m[2][0]*m[0][1]*m[1][2]-m[2][0]*m[1][1]*m[0][2]
    invm=adjm/defm
    return invm

'''
m=np.array([[1,2,3],[4,3,6],[1,8,9]])
print(inv3(m))
print(np.linalg.det(m))
print(np.linalg.inv(m))
'''

def lineCurvature2D(Vertices,Lines):
    '''
    :param Vertices: 共M个点，M*2维【x，y】
    :param Lines: 共N条折线，N*2维【左点，右点】
    :return: M个曲率
    x=a3 t^2+ a2 t+ a1
    y=b3 t^2+ b2 t+ b1
    利用本身点和其前后相邻的两点，拟合以上曲线，并求曲率
    '''
    vertices=np.array(Vertices)
    Na=-np.ones((vertices.shape[0],1))
    Nb=-np.ones((vertices.shape[0],1))
    for line in Lines:
        Na[line[0]]=line[1]
        Nb[line[1]]=line[0]
    for i in range(Na.shape[0]):
        if Na[i]==-1:
            Na[i]=i
        if Nb[i]==-1:
            Nb[i]=i
    Disa=np.zeros((vertices.shape[0],1))
    Disb=np.zeros((vertices.shape[0],1))

    for i in range(Na.shape[0]):
        na_num=Na[i].astype("int8")
        nb_num=Nb[i].astype("int8")
        #print(na_num,nb_num)
        Disa[i]=-length(vertices[i],vertices[na_num[0]])
        Disb[i]=length(vertices[i],vertices[nb_num][0])

    x=np.zeros([vertices.shape[0],3])
    y=np.zeros([vertices.shape[0],3])
    for i in range(vertices.shape[0]):
        na_num = Na[i].astype("int8")
        nb_num = Nb[i].astype("int8")
        x[i][0]=vertices[na_num[0]][0]
        x[i][1] = vertices[i][0]
        x[i][2] = vertices[nb_num[0]][0]
        y[i][0] = vertices[na_num[0]][1]
        y[i][1] = vertices[i][1]
        y[i][2] = vertices[nb_num[0]][1]

    M=np.zeros([vertices.shape[0],3,3])
    for i in range(M.shape[0]):
        M[i][0][0]=1
        M[i][0][1]=-Disa[i]
        M[i][0][2]=Disa[i]**2#1 -disa disa**2
        M[i][1][0]=1##100
        M[i][2][0]=1
        M[i][2][1]=-Disb[i]
        M[i][2][2]=Disb[i]**2#1 -disb disb**2
        '''
        x=a3 t^2+ a2 t+ a1
        y=b3 t^2+ b2 t+ b1
        k=2(a2*b3-a3*b2)/((b2**2+a2**2)**(3/2))
        '''
    k=np.zeros((vertices.shape[0],1))
    for i in range(1,vertices.shape[0]-1):
        print(i)
        invm=np.linalg.inv(M[i])
        a2=invm[0][1]*x[i][0]+invm[1][1]*x[i][1]+invm[2][1]*x[i][2]
        a3=invm[0][2]*x[i][0]+invm[1][2]*x[i][1]+invm[2][2]*x[i][2]
        b2 = invm[0][1] * y[i][0] + invm[1][1] * y[i][1] + invm[2][1] * y[i][2]
        b3 = invm[0][2] * y[i][0] + invm[1][2] * y[i][1] + invm[2][2] * y[i][2]
        k[i]=2*(a2*b3-a3*b2)/((a2**2+b2**2)**(3/2))

    return k


vertices=[[2,3],[3,2],[6,9]]
lines=[[0,1],[1,2]]
k=lineCurvature2D(vertices,lines)
print(k)




