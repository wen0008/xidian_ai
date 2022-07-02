a=[1,3,2,3,3,3,4]
def candidate(m,a):
    j=m
    x=a[m]
    count=1
    while j+1<len(a) and count>0:
        j+=1
        if(a[j]==x):
            count+=1
        else:
            count-=1
    if(j==len(a)-1):
        return x
    else:
        return candidate(j+1,a)

x=candidate(0,a)
count=0
for j in range(0,len(a)):
    if(a[j]==x):
        count+=1
if(count>(len(a)/2)):
    print("Majority element is "+str(x))
else:
    print("Majority element is none")