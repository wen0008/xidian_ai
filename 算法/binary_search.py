a=[1  ,4,  5,  7,  8,  9,  10,  12,  15,  22,  23,  27,  32,  35]
x=22
low=0
high=len(a)
j=-1
while(low<high and j==-1):
    mid=int((low+high)/2)
    if(x==a[mid]):
        j=mid
    elif(x<a[mid]):
        high=mid-1
    else:
        low=mid+1
print(j)
