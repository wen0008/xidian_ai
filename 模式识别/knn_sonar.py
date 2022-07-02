from sklearn import svm
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
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
x_train, x_test , y_train, y_test = train_test_split(sonar_x, sonar_y, test_size = 0.7,random_state=3)
knn = KNeighborsClassifier()    #实例化KNN模型
knn.fit(x_train, y_train) 
print("knn准确率为：")
print(knn.score(x_test,y_test))