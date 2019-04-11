import math
try:
    n=input()
    n=n.split()
    l=int(n[0])
    u=int(n[1])
    c=0
    for i in range(l,u):
        s=int(math.pow(i,2))
        if(s>=l and s<=u):
            c=c+1
    for i in range(l):
        s=int(math.pow(i,2))
        if(s>=l and s<=u):
            c=c+1
    print(c)
except:
    print('invalid')
