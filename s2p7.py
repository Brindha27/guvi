import math
try:
    n=int(input())
    if(n<=100000):
        nn=n
        l=[]
        s=0
        while(n>0):
            r=n%10
            l.append(r)
            n=n//10
        p=len(l)
        for i in l:
            s=s+math.pow(i,p)
        if(s==nn):
            print('yes')
        else:
            print('no')
    else:
        print('invalid')
except:
    print('invalid')
