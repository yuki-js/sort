a = list(map(int,input().split()))
n = len(a)

def qsort(arr,left,right):
    
    if left<right:
        i=left
        j=right
        pivot = arr[i+int((j-i)/2)]
        while True:
            while arr[i]<pivot:
                i+=1
            while pivot<arr[j]:
                j-=1
            if i>=j:
                break
            tmp = arr[i]
            arr[i]=arr[j]
            arr[j]=tmp
            i+=1
            j-=1
        qsort(arr,left,i-1)
        qsort(arr,j+1,right)

qsort(a,0,n-1)
#print(a)
