import random
import matplotlib.pyplot as plt

#读入样本数据
fh=open('waveform.data')
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
    lst1.append(lst0[0:len(lst0)-1])
    types.append(lst0[len(lst0)-1])


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
    while(j<len(lst2)):
        datas[i].append(float(lst2[j]))
        j+=1
    j=0
    i+=1

#各取100个
i=0
j=0
k=0
m=0
datas1=list()
types1=list()
while(i<100 or j<100 or k<100):
    if(types[m]=='2' and i<100):
        datas1.append(datas[m])
        types1.append(int(types[m]))
        i+=1
    elif(types[m]=='1' and j<100):
        datas1.append(datas[m])
        types1.append(int(types[m]))
        j+=1
    elif(types[m]=='0' and k<100):
        datas1.append(datas[m])
        types1.append(int(types[m]))
        k+=1
    m+=1
types=types1
datas=datas1
for type in types:
    typesdatas[type]=typesdatas.get(type,0)+1
#print(typesdatas)

#添加高斯噪声
for i in range(len(datas)):
    for j in range(len(datas[i])):
        datas[i][j]+=random.gauss(mu=0, sigma=0.2)

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
#k=int(input("输入k值: "))
k=3
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

def pam(k,mtypes,m,unsure_data=[]):
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

#计算距离
def distance(x,y):
    s=0
    for i in range(len(x)):
        s+=(x[i]-y[i])**2
    z=s**0.5
    return z

#判断前后聚类中心是否相同
def m_is_m0(m,m0):
    i=0
    j=0
    r=True
    while(i<len(m)):
        j+=distance(m[i],m0[i])
        i+=1 
    #print(j)
    if(j>2):
        r=False           
    return(r)   



# pam过程
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
            ktypes.append(pam(k,mtypes,m,datas[j]))
            j+=1
        else:
            ktypes[j]=pam(k,mtypes,m,datas[j])
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
    z=0
    while(z<int(k)):
        m0[z]=(m[z][:])
        z+=1
    z=0
    r=0
    i=0
    j=0
    for key,v in ktypesdatas.items():       #更新聚类中心m
        d=list()
        s=0
        if(len(v)==0):
            continue
        while(j<len(ktypesdatas[key])):
            while(r<len(ktypesdatas[key])):
                s+=distance(datas[ktypesdatas[key][j]],datas[ktypesdatas[key][r]])
                r+=1
            d.append(s)
            j+=1
            r=0
            s=0
        j=0
        m[key]=datas[d.index(min(d))]

    if(m_is_m0(m,m0)):
        break

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
    if(len(ktypesdatas[i])==0):
        i+=1
        continue
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
#画图,以数据的前一半特征和为x，后一半特征和为y
i=0
while(i<len(datas)):
    j=0
    z=0
    while(j<len(datas[0])/2):
        z+=datas[i][j]
        j+=1
    x=z
    z=0
    while(j<len(datas[0])):
        z+=datas[i][j]
        j+=1
    y=z
    if(types[i]==0):plt.scatter(x,y,c='#0000FF')
    elif(types[i]==1):plt.scatter(x,y,c='#9400D3')
    else:plt.scatter(x,y,c='#008000')
    i+=1    
plt.show()
plt.clf()
i=0
while(i<len(ktypesdatas)):
    j=0
    while(j<len(ktypesdatas[i])):
        
        p=0
        z=0
        while(p<len(datas[ktypesdatas[i][j]])/2):
            z+=datas[ktypesdatas[i][j]][p]
            p+=1
        x=z
        z=0
        while(p<len(datas[ktypesdatas[i][j]])):
            z+=datas[ktypesdatas[i][j]][p]
            p+=1
        y=z
        if(i==0):plt.scatter(x,y,c='#0000FF')
        elif(i==1):plt.scatter(x,y,c='#9400D3')
        else:plt.scatter(x,y,c='#008000')
        j+=1        
    i+=1
plt.show()