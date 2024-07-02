import pandas as pd
import numpy as np
import math

arr=np.array([[1,1,0,1,1],
              [0,0,1,1,0],
              [0,1,1,0,0],
              [1,0,0,1,0],
              [1,0,1,0,1],
              [1,0,1,1,0]])
# the block point
a=np.array([[1],
            [1],
            [1],
            [1],
            [1],
            [1]])
#y label
y=np.array([[1],
            [0],
            [1],
            [0],
            [1],
            [0]])

c=np.append(arr,a,axis=1)
df=pd.DataFrame(c)
the=np.array([0,0,0,0,0,0])# theta 0

#func cal theta*x
def theta(the):
    z=[]
    for i in range(0,len(df[0])):
        multiplication=np.dot(the,df[i])
        z.append(multiplication)# 0,0,0,0,0,0
    return z
# func sum the theta, sum=(1/1+e^-theta*xi)*xi
def sum_the(y):
    theta(the)
    s=[]
    for j in range(0, 6):
        for i in range(0,len(theta(the))):
            k=(1/(1+pow(math.e,-theta(the)[i]))-y[i])# 1/1+e^-theta-yi
            d=k*df[j][i]# k*xi
                #s.append(d.mean())
            s.append(d.mean())#append the mean of point
    
    return s

ad=np.array(sum_the(y)).reshape((6,6))#reshape the array
thetaa=[]
for i in range(0,len(ad[0])):
    t=sum(ad[i])*(-0.5)# theta i=theta0-0,5*sum.theta
    thetaa.append(t.mean())

x=thetaa[len(thetaa)-1]
thetaa.pop(len(thetaa)-1)
thetaa.insert(0,x)
thetaa=np.array(thetaa)
print("bộ theta mới: ",thetaa)
#func calculation H0=1/(e^-theta*x)
def hO(thetaa,x):
    cal=1/(1+math.pow(math.e,-np.dot(thetaa,x)))
    return cal

x=np.array([1,0,1,0,0,1])
predict=hO(thetaa,x)
if predict>=0.5:
    print("giá trị tính toán được: {}".format(predict),"\nkết quả bộ dự đoán: 1",)
else:
    print("giá trị tính toán được: {}".format(predict), "\nkết quả bộ dự đoán: 0", )
