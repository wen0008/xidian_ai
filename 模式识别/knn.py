import numpy
#读入样本数据
fh=open('iris.txt')
lst0=list()
lst1=list()
datas=list()
types=list()
i=0
j=0
for line in fh:
    line=line.rstrip()
    lst0=line.split(',')
    if(lst0==['']):
        break
    lst1.append(lst0[0:4])
    types.append(lst0[4])

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
#print(datas)

#特征归一化
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
#print(Max)
#print(Min)
#print(M)


#计算距离
def distance(M=[],unsure_data=[],sure_data=[[]]):   
    udata=numpy.array(unsure_data)
    sdata=numpy.array(sure_data)
    m=numpy.array(M)
    j=0
    i=0
    dis=list()
    while(i<len(sure_data)):
        d=0
        while(j<len(sure_data[0])):
            d+=((udata[j]-sdata[i][j])**2)/(m[j]**2)        #这直接用list[j]形式计算会报错unsupported operand type(s) for -: 'float' and 'list'，不知道为啥
            j+=1
        j=0
        i+=1
        dis.append(d**0.5)   
    return(dis)

#knn算法,输入一个样本，输出识别结果
def knn(k,unsure_data=[],sure_data=[[]],sure_types=[]):
    dis0=distance(M,unsure_data,datas)
    i=0
    dis1=list()
    while(i<len(dis0)):
        dis1.append(dis0[i].tolist())
        i+=1
    #print(dis1)
    dis1=sorted(dis0)
    typ0=list()
    i=0
    while(i<k):
        ind=dis0.index(dis1[i])
        typ0.append(ind)           #typ0是前k距离的索引
        i+=1
    unsure_type=dict()
    unsure_type['Iris-setosa']=0
    unsure_type['Iris-versicolor']=0
    unsure_type['Iris-virginica']=0
    i=0
    while(i<k):
        if(types[typ0[i]]=='Iris-setosa'):
            unsure_type['Iris-setosa']+=1
        if(types[typ0[i]]=='Iris-versicolor'):
            unsure_type['Iris-versicolor']+=1
        if(types[typ0[i]]=='Iris-virginica'):
            unsure_type['Iris-virginica']+=1    
        i+=1   
    stype=max(unsure_type,key=unsure_type.get)  #找到字典中最大值对应的键，key在这里是一个函数，相当于比较的是经过key后面这个函数映射后的集合，返回对应的键
    return stype        


#读入转换测试数据
fh1=open('test_iris.txt')
j=0
i=0
t_lst=list()
t_types=list()
t_datas=list()
for line in fh1:
    line=line.rstrip()
    lst0=line.split(',')
    if(lst0==['']):
        break
    t_lst.append(lst0[0:4])
    t_types.append(lst0[4])

lst3=list()
t_data=list()
while(i<len(t_types)):
    t_datas.append(list())
    i+=1
i=0
while(i<len(t_lst)):
    while(j<len(t_lst[0])):
        if(i==0):
            lst3.append(float(lst1[i][j]))
            j+=1
            continue
        lst3[j]=float(t_lst[i][j])
        j+=1
    j=0
    while(j<len(t_lst[0])):
        t_datas[i].append(float(lst3[j]))
        j+=1
    j=0
    i+=1
#print(t_datas)


#测试数据计算
i=0
j=0
true=0
accuracy=0
k=int(input('输入k值： '))
result=list()
while(i<len(t_datas)):
    result.append(knn(k,t_datas[i],datas,types))
    i+=1
print(result)
while(j<len(result)):
    if(result[j]==t_types[j]):
        true+=1
    j+=1    
accuracy=true/len(result)
print('accuracy='+str(accuracy))
