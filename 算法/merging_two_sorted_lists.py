a=[5,8,11,4,8,10,12]
b=[0,0,0,0,0,0,0]
p=0
q=2
r=6
s=p
t=q+1
k=p
while(s<=q and t<=r):
    if(a[s]<=a[t]):
        b[k]=a[s]
        s+=1
    else:
        b[k]=a[t]
        t+=1
    k+=1
#循环结束后还剩下a[6]=12
if(s==q+1):
    b[k]=a[t]
else:
    b[k]=a[s]    
print(b)
    
