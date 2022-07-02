import numpy as np
import pickle
import os
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow 
from sklearn.decomposition import PCA
import torch
from PIL import Image
#加载数据（读取batch1中的10000幅图）
CIFAR_DIR = "cifar-10-batches-py"
#print(os.listdir(CIFAR_DIR))
with open(os.path.join(CIFAR_DIR, "data_batch_1"), 'rb') as f:
	data = pickle.load(f, encoding='bytes')
"""#展示数据集    
	print(type(data))
	print(data.keys())
	print(type(data[b'data']))
	print(type(data[b'labels']))
	print(type(data[b'batch_label']))
	print(type(data[b'filenames']))
	print(data[b'data'].shape)
	print(data[b'data'][2:4])
	print(data[b'batch_label'])
	print(data[b'filenames'][2:4])
image = data[b'data'][0]
print(data[b'labels'][0])
image = image.reshape((3,32,32)) #32 32 3
image = image.transpose((1,2,0))
imshow(image)
plt.show()"""
imgdata=data[b'data'][:]
imglabel=data[b'labels'][:]
ldata=dict()
lendata=len(imgdata)
for j in range(10):
    ldata[j]=0
for i in range(len(imgdata)):
    for j in range(10):
        if(int(imglabel[i])==j):
            ldata[j]+=1
print("各类图片数量：")
print(ldata)
def to_gray(data):
    d=data.reshape((3,32,32))
    d1=(30*d[0]+59*d[1]+11*d[2]+50)/100
    return d1

def generate_code(data, R, code_length = 128):  #编码
    pca = PCA(n_components=code_length)
    p=pca.fit_transform(data)
    return (torch.from_numpy(p).float().to(R.device) @ R).sign()
def itq(data,code_length = 128,max_iter = 50,
        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu"),):  #计算itq算法编码方式
    R = torch.randn(code_length, code_length).to(device)
    [U, _, _] = torch.svd(R)
    R = U[:, :code_length]
    pca = PCA(n_components=code_length)
    #print(pca.fit_transform(data))
    V = torch.from_numpy(pca.fit_transform(data)).float().to(device)
    # Training
    for i in range(max_iter):
        V_tilde = V @ R
        B = V_tilde.sign()
        [U, _, VT] = torch.svd(B.t() @ V)
        R = (VT.t() @ U.t())
    code = np.array(generate_code(data,R,code_length=code_length).to(torch.device('cpu')))
    return code
def hamming(b1,b2): #计算汉明距离
    l=len(b1)
    if(l!=len(b2)):return False
    d=0
    for i in range(l):
        if(b1[i]!=b2[i]):d+=1
    return d
def search(target,imgcode,maxiter=5,sacc=48):   #搜索目标图片过程
    result=list()
    lendata=len(imgcode)
    r=list()
    for j in range(maxiter):
        for i in range(lendata):
            if(hamming(imgcode[target[j]],imgcode[i])<sacc):r.append(1)
            else: r.append(0)
        result.append(r)
        r=list()
    for i in range(lendata):
        t=0
        for j in range(maxiter):
            if(result[j][i]==1):
                t+=1
        if(t>maxiter/2):r.append(1)
        else:r.append(0)
    return r
def imgreshape(r):  #将图片转换为可展示的格式
    image = r.reshape((3,32,32)) #32 32 3
    image = image.transpose((1,2,0))
    return image

d=imgdata[:]
imgcode=itq(d,code_length=128)
target=list()
targetlabel=6
maxiter=50
print("目标为第{}类图片".format(targetlabel))
for i in range(maxiter):
    if(i==0):t=0
    r=t+1
    t=imglabel.index(targetlabel,r)
    target.append(t)
result=search(target,imgcode,maxiter)
acc=0
res=0
for i in range(lendata):
    if(result[i]==1 and imglabel[i]==imglabel[t]):acc+=1
    if(result[i]==1):res+=1
print("正确标记数：{}".format(acc))
print("标记总数：{}".format(res))
wd=acc/ldata[imglabel[t]]
acc/=res
print("精度为:{}".format(acc))
print("广度为:{}".format(wd))
#可视化
for i in range(100):
    if(i<10):
        plt.subplot(10,10,i+1)
        plt.imshow(imgreshape(imgdata[target[i]]))
        plt.title("torget",fontsize=8)
        plt.xticks([])
        plt.yticks([])
    else:
        if(i==10):t=0
        r=t+1
        t=result.index(1,r)
        plt.subplot(10,10,i+1)
        plt.imshow(imgreshape(imgdata[r]))
        plt.xticks([])
        plt.yticks([])
plt.show()