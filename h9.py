try:
    n=int(input())
    m=input()
    m=m.split()
    l=[]
    res=[]
    for i in m:
        l.append(int(i))
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            s=l[i]+l[j]
            if s==0:
                res.append(l[i])
                res.append(l[j])
    print(res[0],end=' ')
    print(res[1],end=' ')
        
except:
    print('invalid')
