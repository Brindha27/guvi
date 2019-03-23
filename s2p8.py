import math
try:
    n=input()
    n=n.split()
    i=int(n[0])
    j=int(n[1])
    res=[]
    for a in range(i+1,j):
        nn=a
        l=[]
        s=0
        while(a>0):
            r=a%10
            l.append(r)
            a=a//10
        p=len(l)
        for i in l:
            s=s+math.pow(i,p)
        if(s==nn):
            res.append(nn)
    for i in range(len(res)-1):
        print(res[i],end=' ')
    print(res[-1])
except:
    print('invalid')
