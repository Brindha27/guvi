
try:
    n=int(input())
    m=input()
    b='-1'
    m=m.split()
    l=[]
    a=[]
    for i in m:
        l.append(int(i))
    for i in range(len(l)):
        if(i==l[i]):
            a.append(l[i])
    if(len(a)>0):
        a.sort()
        for i in range(len(a)-1):
            print(a[i],end=' ')
        print(a[-1])
    else:
        print(b)
except:
    print('invalid')
