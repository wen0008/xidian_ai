lst=[1,3,2,3,3,4,3,4,6,3,1,3,3,3,3]
count=0
c=lst[0]

def candidate(m,list=[]):
    j=m
    n=len(list)
    c=list[m]
    count=1
    while(j<n and count>0):
        
        if(list[j]==c):
            count+=1
        else:
            count-=1
        j+=1
    if(j==n):
        return c
    else:
        return(candidate(j+1,list))    

n=len(lst)
c=candidate(0,lst)
count=0
j=0
while(j<n):
    if(lst[j]==c):
        count+=1
    j+=1
if(count>=n/2):
    print(c)
else:
    print('none')            