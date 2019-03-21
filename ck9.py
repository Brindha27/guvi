try:
    n1=input()
    n2=input()
    n1=n1.split()
    l1=[]
    for i in n1:
        l1.append(int(i))
    s=l1[0]
    r=l1[1]
    n2=n2.split()
    l=len(n2)
    r1=[]
    res=0
    if(l==s):
        for i in range(l):
            r1.append(int(n2[i]))
        for i in range(0,r):
            res=res+r1[i]
        print(res)
    else:
        print('invalid')
    
except:
    print('invalid')
