from sklearn.ensemble import BaggingClassifier
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split 
iris = datasets.load_iris()
iris_x = iris.data
iris_y = iris.target
#print(iris_x)
#print(iris_y)
x_train, x_test , y_train, y_test = train_test_split(iris_x, iris_y, test_size = 0.3)
bagging=BaggingClassifier(KNeighborsClassifier(),bootstrap=True,max_samples=0.3, max_features=0.3)
bagging.fit(x_train,y_train)
y_pred=bagging.predict(x_test)
print("测试集类别为:")
print(y_test)
print("预测类别为:")
print(y_pred)
accuracy=0
i=0
while(i<len(y_test)):
    if(y_test[i]==y_pred[i]):
        accuracy+=1
    i+=1    
accuracy/=len(y_test)
print("accuracy="+str(accuracy))