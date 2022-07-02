import numpy as np
import PIL.Image as image
from sklearn.cluster import KMeans
import random
import skimage
from skimage import io
from skimage import util
def load(path):
    f=open(path,'rb')
    data=[]
    img=image.open(f)
    m,n=img.size
    i=0
    while(i<m):
        j=0
        while(j<n):
            x,y,z=img.getpixel((i,j))
            data.append([x/256.0,y/256.0,z/256.0])
            j+=1
        i+=1
    return np.mat(data),m,n

image0=io.imread("426.jpg")
image1=util.random_noise(image0, mode='gaussian', var=0.1) #添加高斯噪声
io.imsave("pic_noisy.jpg",image1)

imgdata,row,col=load("426.jpg")
imgdata1,row1,col1=load("pic_noisy.jpg")
km=KMeans(n_clusters=5)
label=km.fit_predict(imgdata)
label=label.reshape([row,col])
newpic=image.new("L",(row,col))
label1=km.fit_predict(imgdata1)
label1=label1.reshape([row1,col1])
newpic1=image.new("L",(row1,col1))
i=0
while(i<row):
    j=0
    while(j<col):
        newpic.putpixel((i,j),int(256/(label[i][j]+1)))
        newpic1.putpixel((i,j),int(256/(label1[i][j]+1)))
        j+=1
    i+=1
newpic.save("result.jpg","JPEG")
newpic1.save("result1.jpg","JPEG")