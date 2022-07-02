a=[2,4,1,0,5,7,35,11,9,6,5,3,1,2]
def split(a,low,high):
    i=low
    x=a[low]
    for j in range(low+1,high+1):
        if(a[j]<=x):
            i+=1
            if(i!=j):
                c=a[i]
                a[i]=a[j]
                a[j]=c
    c=a[low]
    a[low]=a[i]
    a[i]=c
    w=i
    return(a,w)
def quicksort(a,low,high):    
    if(low<high):
        a,w=split(a,low,high)
        quicksort(a,low,w-1)
        quicksort(a,w+1,high)

low=0
high=len(a)-1
quicksort(a,low,high)
print(a)