try:
    n=int(input())
    m=input()
    m=m.split()
    l=[]
    res=[]
    for i in m:
        l.append(int(i))
    
    for i in range(len(l)):
        if((i%2)==0):
            if((l[i]%2)!=0):
                res.append(l[i])
        else:
            if((l[i]%2)==0):
                res.append(l[i])
    for i in range(len(res)-1):
        print(res[i],end=' ')
    print(res[-1])
        
except:
    print('invalid')
