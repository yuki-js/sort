a = list(map(int,input().split()))
n = len(a)

def qsort(arr,left,right):
    
    if left<right:
        i=left
        j=right
        pivot = a[i+int((j-i)/2)]
        while True:
            while a[i]<pivot:
                i+=1
            while pivot<a[j]:
                j-=1
            if i>=j:
                break
            tmp = a[i]
            a[i]=a[j]
            a[j]=tmp
            i+=1
            j-=1
        qsort(arr,left,i-1)
        qsort(arr,j+1,right)

qsort(a,0,n-1)
#print(a)
