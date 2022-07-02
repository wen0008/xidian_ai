import os
from scipy.io import loadmat
import numpy as np
import random
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import confusion_matrix
from sklearn.metrics import zero_one_loss
from sklearn.metrics import accuracy_score
def load():
    data_path="files"
    data_mark='FE'
    datas={}
    filenams = os.listdir(data_path)
    for label in filenams:
        path=os.path.join(data_path, label)
        filename=os.listdir(path)
        mat_path=os.path.join(path, filename[0])
        file = loadmat(mat_path)
        for key in file.keys():
            if data_mark in key:
                data=file[key].ravel()
        datas[int(label)]=data

    return datas

def data_augment(fs, win_tlen, overlap_rate, datas):
    overlap_rate = int(overlap_rate)
    win_len = int(fs * win_tlen)
    overlap_len = int(win_len * overlap_rate / 100)
    step_len = int(win_len - overlap_len)
    X=[]
    Y=[]
    for label in datas.keys():
        data=datas[label]
        len_data=np.shape(data)[0]
        for start_ind, end_ind in zip(range(0, len_data - win_len, step_len),
                                      range(win_len, len_data, step_len)):
            X.append(data[start_ind:end_ind].ravel())
            Y.append(label)

    X = np.array(X)
    Y = np.array(Y)

    return X,Y
def under_sample_for_c0(X, Y, low_c0, high_c0, random_seed):
    np.random.seed(random_seed)
    to_drop_ind = random.sample(range(low_c0, high_c0), (high_c0 - low_c0 + 1) - len(Y[Y == 3]))
    X = np.delete(X, to_drop_ind, 0)
    Y = np.delete(Y, to_drop_ind, 0)
    return X,Y
def preprocess( fs, win_tlen, overlap_rate, random_seed, **kargs):
    datas=load()
    #X为数据集，采样为1024个点
    X,Y =data_augment(fs, win_tlen, overlap_rate, datas, **kargs)
    low_c0 = np.min(np.argwhere(Y == 0))
    high_c0 = np.max(np.argwhere(Y==0))
    X, Y = under_sample_for_c0(X, Y, low_c0, high_c0, random_seed)
    return X,Y

if __name__ == '__main__':
    epochs = 20
    batch_size = 128
    len_data=1024
    overlap_rate=50
    random_seed=219
    fs=12000
    BatchNorm = True
    num_classes = 10
    X, Y=preprocess( fs, len_data/fs, overlap_rate, random_seed)
    X_train,X_test,y_train,y_test=train_test_split(X, Y, test_size=0.3)
    X_test,X_valid,y_test,y_valid=train_test_split(X_test,y_test,test_size=0.666) #训练：验证：测试=7：2：1
    svm_clf=svm.SVC(kernel='rbf',C=5.3,gamma=0.06)
    svm_clf.fit(X_train,y_train)
    y_pred=svm_clf.predict(X_valid)
    y_pred1=svm_clf.predict(X_test)
    print("验证集分类结果:")
    print(y_pred)
    print("验证集准确率:")
    print(accuracy_score(y_valid,y_pred))
    print("验证集损失率:")
    print(zero_one_loss(y_valid,y_pred))
    C=confusion_matrix(y_valid, y_pred)    
    print("验证集混淆矩阵为:")
    print(C)
    print("测试集准确率:")
    print(accuracy_score(y_test,y_pred1))