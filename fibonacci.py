
import sys
lst = []
n = int(sys.stdin.readline())

for i in range(0,n):
    m = int(sys.stdin.readline())
    lst.append(m)
def fact(a,b):
    
    while(b):
        if b==0:
            break
        else:
            a,b = b,a % b
    return a        
for i in range(0,n):
    a=1
    b=2
    while(1):
        c = fact(lst[i],b)
        if c==1:
            a,b = b, a+b
        else:
            print b,c
            break

    
    

