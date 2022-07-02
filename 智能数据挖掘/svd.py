from sklearn import decomposition
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
musk=open('D:\code\python\learn\musk\clean1.data')
listx=list()
listy=list()
j=0
for line in musk:
    line=line.rstrip()
    line=line.split(',')
    if(line==[" "]):
        break
    i=0
    listx.append(list())
    while(i<len(line)):
        if(i==0):
            if(line[i][:4]=="MUSK"):
                listy.append(1)
            else:
                listy.append(0)
        elif(i==1):
            i+=1
            continue
        else:
            listx[j].append(float(line[i]))
        i+=1
    j+=1
musk_x=np.array(listx)
musk_y=np.array(listy)
musk_x_pca=decomposition.TruncatedSVD(30).fit_transform(musk_x) 
print("原特征向量(以第一项为例):")
print(musk_x[0])
print("特征向量维度:")
print(len(musk_x[0]))
print("提取后：")
print(musk_x_pca[0])
print("维度：")
print(len(musk_x_pca[0]))
musk_x_train1,musk_x_test1,musk_y_train1,musk_y_test1=train_test_split(musk_x,musk_y,test_size=0.3)
musk_x_train2,musk_x_test2,musk_y_train2,musk_y_test2=train_test_split(musk_x_pca,musk_y,test_size=0.3)
svm1=svm.SVC()
svm2=svm.SVC()
clf1=svm1.fit(musk_x_train1,musk_y_train1)
clf2=svm2.fit(musk_x_train2,musk_y_train2)
print("使用svm进行分类测试:")
print("原特征分类准确率:")
print(clf1.score(musk_x_test1,musk_y_test1))
print("提取后准确率:")
print(clf2.score(musk_x_test2,musk_y_test2))
plt.title("提取后盒图")
plt.xlabel("musk_x")
plt.ylabel("value")
plt.boxplot(musk_x_pca,sym="o",whis=1.5)
plt.show()