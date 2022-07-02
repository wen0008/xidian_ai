from sklearn import svm
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.preprocessing import Normalizer
normalizer = Normalizer(norm= 'l1')
from sklearn.ensemble import BaggingClassifier
#从本地读取数据
sonar=open('D:\code\python\learn\模式识别\sonar.txt')
listx=list()
listy=list()
j=0
for line in sonar:
    line=line.rstrip()
    line=line.split(',')
    if(line==['']):
        break
    i=0
    listx.append(list())
    while(i<len(line)):
        if(i+1==len(line)):
            if(line[i]=='R'):
                listy.append(1)
                break
            if(line[i]=='M'):
                listy.append(2)    
                break
        listx[j].append(float(line[i]))
        i+=1
    j+=1
sonar_x=np.array(listx)
sonar_y=np.array(listy)
sonar_x = normalizer.fit_transform(sonar_x)
x_train, x_test , y_train, y_test = train_test_split(sonar_x, sonar_y, test_size = 0.7,random_state=3)#划分测试集和训练集，为观察测试效果选择相同的随机数种子
bagging=BaggingClassifier(svm.SVC(kernel="poly",C=5,degree=30),bootstrap=True,max_samples=0.3, max_features=0.3)
svm_clf=svm.SVC(kernel="poly",C=5,degree=5)
svm_clf.fit(x_train,y_train)#训练svm
bagging_clf=bagging.fit(x_train,y_train)
y_pred=svm_clf.predict(x_test)
print("训练集准确率为：")
print(bagging_clf.score(x_train,y_train))
print("测试集准确率为：")
print(bagging_clf.score(x_test,y_test))