from sklearn import tree 
from sklearn.model_selection import train_test_split
import sys 
import os       
sports=[0,0,1,1,1,0,1,0,1,1,1,1,1,0]  #1为适合运动，0为不适合
# 天气因素，依次为天气（0为晴，1为多云，2为有雨），温度（具体值），湿度（具体值），风况（0为无，1为有）
weather=[[0,85,85,0],
        [0,80,90,1],
        [1,83,78,0],
        [2,70,96,0],
        [2,68,80,0],
        [2,65,70,1],
        [1,64,65,1],
        [0,72,95,0],
        [0,69,70,0],
        [2,75,80,0],
        [0,75,70,1],
        [1,72,90,1],
        [1,81,75,0],
        [2,71,80,1],]
weather_train,weather_test,sports_train,sports_test=train_test_split(weather,sports,test_size=0.2)
clf=tree.DecisionTreeClassifier()
clf=clf.fit(weather_train,sports_train)
result=list()
result=clf.predict(weather_test)
print("预测结果:")
print(result)
print("实际结果:")
print(sports_test)
with open("sports.dot", 'w') as f:
    f = tree.export_graphviz(clf, out_file=f)