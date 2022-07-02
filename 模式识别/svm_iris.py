from sklearn import datasets,svm
from sklearn.model_selection import train_test_split
iris = datasets.load_iris()
iris_x = iris.data[:]
iris_y = iris.target[:]   
print(iris_x)
x_train, x_test , y_train, y_test = train_test_split(iris_x, iris_y, test_size = 0.5)
c=1
svm_clf1=svm.SVC(kernel='linear',C=c)
svm_clf2=svm.SVC(kernel='poly',C=c)
svm_clf3=svm.SVC(kernel='rbf',C=c)
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