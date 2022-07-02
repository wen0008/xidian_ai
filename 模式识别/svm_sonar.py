from sklearn import svm
from sklearn.model_selection import train_test_split
import numpy as np
sonar=open('sonar.txt')
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
x_train, x_test , y_train, y_test = train_test_split(sonar_x, sonar_y, test_size = 0.5,random_state=3)
c=3
svm_clf1=svm.SVC(kernel="linear",C=c)
svm_clf2=svm.SVC(kernel="poly",C=c,degree=5)
svm_clf3=svm.SVC(kernel="rbf",C=c)
svm_clf1.fit(x_train,y_train)
svm_clf2.fit(x_train,y_train)
svm_clf3.fit(x_train,y_train)
y_pred1=svm_clf1.predict(x_test)
y_pred2=svm_clf2.predict(x_test)
y_pred3=svm_clf3.predict(x_test)
print("测试集标签为：")
print(y_test)
print("线性核函数预测结果：")
print(y_pred1)
print("多项式核函数预测结果：")
print(y_pred2)
print("高斯核函数预测结果：")
print(y_pred3)
print("准确率分别为：")
print(svm_clf1.score(x_test,y_test))
print(svm_clf2.score(x_test,y_test))
print(svm_clf3.score(x_test,y_test))