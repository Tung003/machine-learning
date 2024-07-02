import pandas as pd
import numpy as np
import math

df=pd.read_excel("Book1.xlsx")
df=pd.DataFrame(df)

mapping={"nắng":2,"mưa":0,"u ám":1,"nóng":2,"lạnh":0,"trung bình":1,"bình thường":0,"cao":1,"mạnh":1,"yếu":0,"không":0,"có":1}
df["trời"]=df["trời"].map(mapping)
df["nhiệt độ"]=df["nhiệt độ"].map(mapping)
df["độ ẩm"]=df["độ ẩm"].map(mapping)
df["gió"]=df["gió"].map(mapping)
df["chơi tenis"]=df["chơi tenis"].map(mapping)
df=df.drop(columns=["ngày"])
y_labels=df["chơi tenis"]
print(df)
encode={"nắng":2,"mưa":0,"u ám":1,"nóng":2,"lạnh":0,"trung bình":1,"bình thường":0,"cao":1,"mạnh":1,"yếu":0,"không":0,"có":1}

def entropy_root(array):
    kgm=len(array)
    n=0
    m=0
    for i in range(0,kgm):
        if array[i]==1:
            n=n+1
        else:
            m=m+1
    sumary=-(n/kgm)*math.log2(n/kgm)-(m/kgm)*math.log2(m/kgm)
    return sumary

def count_quality(name):# create func for count quality the mean ex 0,0,1,2,2=>3
    count=df[name].nunique()
    return count

def entropy_node(name_parent,name_child):# trả ra các vị trí có giá trị là nắng mưa hoặc u ám trong cột trời
    index=[]
    df1 = df.drop(df[df["trời"] == 0].index)###
    df2 = df1.drop(df[df["trời"] == 1].index)# dataframe drop độ ẩm thấp###

    for i in range(0,len(df2[name_parent])):
        if df[name_parent][i]==name_child:
            index.append(i)
    return index

def entro(name_parent,name_child):# từ vị trí tìm được ta đem gióng sang cột labels xem là giá trị nào đếm giá trị o, 1
    n = []
    m = []
    kgm=len(entropy_node(name_parent,name_child)) #không gian mẫu
    for i in entropy_node(name_parent,name_child):#trả ra giá trị index có là nắng
        if df["chơi tenis"][i]==1:
            n.append(i)#các giá trị có đi chơi
        else:
            m.append(i)#không chơi
    # nếu có trường hợp là tất cả đều có giá trị chơi thì để =0
    if len(n)!=0 and len(m)!=0:
        add = math.log2(len(n) / kgm)
        sub = math.log2(len(m) / kgm)
    elif len(n)==0:
        add=0
    elif len(m)==0:
        sub=0
    sumary = -(((len(n) / kgm) * add) +((len(m) / kgm) * sub))
    return sumary

def IG(a,b,c,d):#độ tăng thông tin IG
    #k=np.array(df["chơi tenis"])
    df1 = df.drop(df[df["trời"] == 0].index)
    df2 = df1.drop(df[df["trời"] == 1].index)# dataframe drop độ ẩm thấp
    print(df2)
    k = np.array(df2["chơi tenis"])
    print("k: ",k)
    h_outlook=entropy_root(k)
    if d=="":
        h_sunny, sun = entro(a, b), entropy_node(a, b)
        h_overcas, cast = entro(a, c), entropy_node(a, c)
        print("x1: ",h_sunny,"x2: ",sun)
        print("y1: ", h_overcas,"y2: ",cast)
        IG_outlook = h_outlook - (h_sunny * len(sun) / len(k) + h_overcas * len(cast) /len(k))
    else:
        h_sunny, sun = entro(a, b), entropy_node(a, b)
        h_overcas, cast = entro(a, c), entropy_node(a, c)
        h_rainy, rain = entro(a, d), entropy_node(a, d)
        print("x1: ",h_sunny,"x2: ",sun)
        print("y1: ", h_overcas,"y2: ",cast)
        print("z1: ", h_rainy,"z2: ",rain)
        IG_outlook=h_outlook-(h_sunny*(len(sun)/len(k))+h_rainy*(len(rain)/len(k))+h_overcas*(len(cast)/len(k)))
    return IG_outlook

def find_root(a,b,c,d):# tìm gốc hoặc nút tiếp theo
    #x=IG("trời",2,1,0)
    y=IG("nhiệt độ",2,1,0)
    z=IG("độ ẩm",1,0,"")
    h=IG("gió",1,0,"")
    arrayy=[]
    #arrayy.append(x)
    arrayy.append(y)
    arrayy.append(z)
    arrayy.append(h)
    maxy=max(arrayy)
    #print("trời: ",x)
    print("IG_nhiệt độ: ",y)
    print("IG_độ ẩm: ",z)
    print("IG_gió: ",h)

    ind=arrayy.index(maxy)
    return maxy,ind

def next_root(df,a):
    x=entropy_node("độ ẩm",1)#độ ẩm cao
    y=entropy_node("độ ẩm",0)#độ ẩm thấp
    #df=df.drop(columns=["độ ẩm"])



x,y=find_root(0,0,0,0)
