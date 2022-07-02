import random

from numpy.lib.function_base import append

#读入样本数据
fh=open('iris1.txt')
lst0=list()
lst1=list()
datas=list()
types=list()
typesdatas=dict()#样本类型统计（各类型数量）
i=0
j=0
for line in fh:
    line=line.rstrip()
    lst0=line.split(',')
    if(lst0==['']):
        break
    lst1.append(lst0[0:4])
    types.append(lst0[4])
for type in types:
    typesdatas[type]=typesdatas.get(type,0)+1
#print(typesdatas)

#数据类型转换为float
lst2=list()
while(i<len(lst1)):
    datas.append(list())
    i+=1
i=0
while(i<len(lst1)):
    while(j<len(lst1[0])):
        if(i==0):
            lst2.append(float(lst1[i][j]))
            j+=1
            continue
        lst2[j]=float(lst1[i][j])
        j+=1
    j=0
    while(j<4):
        datas[i].append(float(lst2[j]))
        j+=1
    j=0
    i+=1

#"""
#特征归一化M
Max=datas[0][:]
Min=datas[0][:]
i=0
j=0
while(i<len(datas)):
    while(j<len(datas[0])):
        if(Max[j]<datas[i][j]):
            Max[j]=datas[i][j]
        if(Min[j]>datas[i][j]):
            Min[j]=datas[i][j]
        j+=1
    i+=1
    j=0            
M=list()
j=0
while(j<len(datas[0])):
    M.append(Max[j]-Min[j])
    j+=1
i=0
j=0
while(i<len(datas)):
    while(j<len(datas[0])):
        datas[i][j]/=M[j]
        j+=1
    j=0
    i+=1    
#""" 

#初始化聚类中心(随机产生)
k=int(input("输入k值: "))
i=0
j=0
m=list()      #m为聚类中心
m0=list()
mtypes=list()
mtruetypes=list()
while(i<int(k)):
    r=random.randint(0,len(datas)-1)
    m.append(datas[r])
    mtruetypes.append(types[r])
    mtypes.append(i)
    i+=1
i=0
print("初始聚类中心：")
print(m)
print(mtruetypes)
while(i<int(k)):
    m0.append(list())
    m0[i]=(m[i][:])
    i+=1
#k_means聚类，输入一个样本，输出聚类结果
def kmeans(k,mtypes,m,unsure_data=[]):
    i=0
    j=0
    d=0
    distance=list()
    while(i<k):
        while(j<len(m[0])):
            d+=(unsure_data[j]-m[i][j])**2
            j+=1
        distance.append(d**0.5)
        i+=1
        d=0
        j=0
    ktype=mtypes[distance.index(min(distance))]    
    return(ktype)    

#判断前后聚类中心是否相同
def m_is_m0(m,m0):
    i=0
    j=0
    r=True
    while(i<len(m)):
        if(m[i] not in m0):
            r=False
            break
        i+=1    
    return(r)   


# kmeans过程
i=0
j=0
ktypes=list()
ktypesdatas=dict()
sum=dict()
while(i<int(k)):
    sum[i]=list()
    while(j<len(datas[0])):
        sum[i].append(0)
        j+=1
    j=0
    i+=1       
i=0
j=0
while(True):
    j=0         #清空ktypesdatas
    while(j<int(k)):
        ktypesdatas[j]=list()
        j+=1
    j=0
    while(j<len(datas)):       #聚类
        if(len(ktypes)<len(types)):
            ktypes.append(kmeans(k,mtypes,m,datas[j]))
            j+=1
        else:
            ktypes[j]=kmeans(k,mtypes,m,datas[j])
            j+=1
    j=0
    i=0
    while(i<len(ktypes)):
        for key,v in ktypesdatas.items():
            if(ktypes[i]==key):
                ktypesdatas[key].append(i)
                i+=1
                break     

    for key,v in sum.items():      #清空sum
        j=0
        while(j<len(sum[key])):
            sum[key][j]=0
            j+=1

    r=0
    i=0
    j=0
    for key,v in ktypesdatas.items():       #更新聚类中心m
        if(len(v)==0):
            continue
        while(j<len(ktypesdatas[key])):
            while(r<len(datas[0])):
                sum[key][r]+=datas[ktypesdatas[key][j]][r]
                r+=1
            j+=1
            r=0
        j=0
    j=0
    for key,v in sum.items():
        while(r<len(datas[0])):
            if(len(ktypesdatas[key])==0):
                break
            m[j][r]=sum[key][r]/len(ktypesdatas[key])
            r+=1
        j+=1
        r=0
    if(m_is_m0(m,m0)):
        break
    z=0
    while(z<int(k)):
        m0[z]=(m[z][:])
        z+=1
    z=0

#统计纯度
i=0
j=0
result=list()
while(i<k):
    result.append(list())
    while(j<k):
        result[i].append(0)
        j+=1
    i+=1
    j=0    

for key,v in ktypesdatas.items():
    i=0
    j=0
    while(i<len(ktypesdatas[key])):
        if(ktypesdatas[key][i]<50):
            result[key][0]+=1
        elif(ktypesdatas[key][i]<100):
            result[key][1]+=1
        else:
            result[key][2]+=1
        i+=1        
i=0
purity=list()    #纯度(正确聚类的文档数占总文档的比例) 
while(i<k+1):
    purity.append(0)
    i+=1
i=0
j=0
pn=0
while(i<len(result)):
    if(result[i].index(max(result[i]))==0):
        pn+=result[i][0]
        purity[j+1]=result[i][0]/len(ktypesdatas[i])
    elif(result[i].index(max(result[i]))==1):
        pn+=result[i][1]
        purity[j+2]=result[i][1]/len(ktypesdatas[i])
    else:
        pn+=result[i][2]
        purity[j+3]=result[i][2]/len(ktypesdatas[i])
    i+=1
purity[0]=pn/len(ktypes)

print("聚类结果：")
print(ktypesdatas)
print("总纯度为"+str(purity[0]))
print("第一类样本纯度为"+str(purity[1]))
print("第二类样本纯度为"+str(purity[2]))
print("第三类样本纯度为"+str(purity[3]))