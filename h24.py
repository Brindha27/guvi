try:
    n=input()
    m=input()
    n=n.split()
    m=m.split()
    le=int(n[0])
    r=int(n[1])
    l=[]
    f,s=0,0
    for i in m:
        l.append(int(i))
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            s=l[i]+l[j]
            if(s==r):
                f=1
    if(f==1):
        print('YES')
    else:
        print('NO')
except:
    print('invalid')
