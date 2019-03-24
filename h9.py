try:
    n=int(input())
    m=input()
    m=m.split()
    l=[]
    res=[]
    res1=[]
    res2=[]
    for i in m:
        l.append(int(i))
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            s=l[i]+l[j]
            if s==0:
                res.append([l[i],l[j]])
            else:
                res1.append([l[i],l[j]])
                res2.append(s)
    a=min(res2)
    b=res2.index(a)
    if(len(res)>0):
        print(res[0][0],end=' ')
        print(res[0][1])
    else:
        print(res1[b][0],end=' ')
        print(res1[b][1])
        
except:
    print('invalid')
