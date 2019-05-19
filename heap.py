a = list(map(int,input().split()))

def heapsort(arr,e):
    i=1
    while i<e:
        upheap(arr,i)
        i+=1
    i-=1
    while i>0:
        tmp=arr[0]
        arr[0]=arr[i]
        arr[i]=tmp
        i-=1
        downheap(arr,i)

def leftC(i):
    return int(((i) + 1) * 2 - 1)
def rightC(i):
    return int(((i) + 1) * 2)
def parent(i):
    return int(((i) + 1) / 2 - 1)

def upheap(arr,n):
    while n>0:
        m = parent(n)
        if arr[m]<arr[n]:
            tmp=arr[m]
            arr[m]=arr[n]
            arr[n]=tmp
        else:
            break
        n=m

def downheap(arr,n):
    m=0
    tmp=0

    while True:
        lc=leftC(m)
        rc=rightC(m)
        if lc>=n:
            
            break
        if arr[lc]>arr[tmp]:
            tmp=lc
        if rc<n and arr[rc]>arr[tmp]:
            tmp=rc
        if tmp==m:
            break
        swp=arr[tmp]
        arr[tmp]=arr[m]
        arr[m]=swp
        m=tmp

heapsort(a,len(a))
#print(a)
