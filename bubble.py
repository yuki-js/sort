a = list(map(int,input().split()))
n = len(a)

for i in range(0,n):
    for j in range(n-1,i,-1):
        if a[j]<a[j-1] :
            temp = a[j]
            a[j]=a[j-1]
            a[j-1]=temp

#print(a)
