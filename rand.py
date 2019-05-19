import random
import sys

a=""
k=int(sys.argv[1])
for i in range(k):
    a+=(str(random.randrange(0,k,1))+" ")
print(a)
