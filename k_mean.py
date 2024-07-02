import pandas as pd
import matplotlib.pyplot as mpl
import math as _
import numpy as np
"""arr=np.array([[1,10],
              [2,5],
              [8,4],
              [5,8],
              [7,5],
              [6,4],
              [1,2],
              [4,9]])"""
arr=np.array([[1,1],
              [2,1],
              [4,3],
              [5,4]])
c1=np.array([1,1])# khai báo tâm ban đầu
c2=np.array(arr[1])
n1=[]
n2=[]
def distance(arr,n1,n2): # tính toán khoảng cách từ tâm đển các điểm
    for i in range(0,len(arr)):
        a=np.array(arr[i])
        d1=_.sqrt(_.pow(c1[0]-a[0],2)+_.pow(c1[1]-a[1],2))
        d2=_.sqrt(_.pow(c2[0]-a[0],2)+_.pow(c2[1]-a[1],2))
        print("khoảng cách với tâm c1: ",d1)
        print("khoảng cách với tâm c2: ",d2)
        if (d1<d2):
            n1.append(a)
        else:
            n2.append(a)
    return n1,n2

def update_center(n1,n2):# hàm cập nhật lại tâm k_mean
    z1=sum(n1)
    c1=np.array([z1[0]/len(n1),z1[1]/len(n1)])
    z2=sum(n2)
    c2=np.array([z2[0]/len(n2),z2[1]/len(n2)])
    return c1,c2

"""distance(arr,n1,n2)
c1,c2=update_center(n1,n2)
print(c1,"\t",c2)"""

while(True):
    n1,n2=distance(arr, n1, n2)
    c1, c2 = update_center(n1, n2)
    print("tâm cụm 1: ",c1, "\ttâm cụm 2: ", c2)
    n1 = []  # làm rỗng lại mảng
    n2 = []  # làm rỗng lại mảng
    distance(arr, n1, n2)
    g1, g2 = update_center(n1, n2)
    print("tâm cụm 1: ",g1, "\ttâm cụm 2: ", g2)
    if g1.any()==c1.any():
        print("cụm 1 có các điểm sau: ",n1,"\ncụm 2 có các điểm sau: ",n2)
        break
"""
distance(arr,n1,n2)
c1,c2=update_center(n1,n2)
print(c1,"\t",c2)
n1=[]#làm rỗng lại mảng
n2=[]#làm rỗng lại mảng
distance(arr,n1,n2)
c1,c2=update_center(n1,n2)
print(c1,"\t",c2)
n1=[]#làm rỗng lại mảng
n2=[]#làm rỗng lại mảng
distance(arr,n1,n2)
print(n1,"\n",n2)
c1,c2=update_center(n1,n2)
print(c1,"\t",c2)
n1=[]#làm rỗng lại mảng
n2=[]#làm rỗng lại mảng
distance(arr,n1,n2)
print(n1,"\n",n2)
c1,c2=update_center(n1,n2)
print(c1,"\t",c2)"""