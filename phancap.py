import pandas as pd
import math
import numpy as np

arr=np.array([[1,1],
              [1.5,1.5],
              [5,5],
              [3,4],
              [4,4],
              [3,3.5]])

df=pd.DataFrame(arr)
print(df[0])


def distance():
        for i in range(0,len(df[0])):
            if i<5:
                t=i+1
                dist=math.sqrt(math.pow(df[0][i]-df[0][t],2)+math.pow(df[1][i]-df[1][t],2))
                print( dist)
            if i>=0 and i<4:
                t=i+2
                dist = math.sqrt(math.pow(df[0][i] - df[0][t], 2) + math.pow(df[1][i] - df[1][t], 2))
                print(dist)
            if i>=0 and i<3:
                t=i+3
                dist = math.sqrt(math.pow(df[0][i] - df[0][t], 2) + math.pow(df[1][i] - df[1][t], 2))
                print(dist)
            if i>=0 and i<2:
                t=i+4
                dist = math.sqrt(math.pow(df[0][i] - df[0][t], 2) + math.pow(df[1][i] - df[1][t], 2))
                print(dist)
            if i==0:
                t=i+5
                dist=math.sqrt(math.pow(df[0][i]-df[0][t], 2) + math.pow(df[1][i] - df[1][t], 2))
                print(dist)

distance()