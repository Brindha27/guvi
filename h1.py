try:
    n=int(input())
    i=input()
    i=i.split()
    l=[]
    for j in i:
        l.append(int(j))
    p=[]
    for j in l:
        if (l.count(j)>1):
            p.append(j)
    if(len(p)>0):
        p=set(p)
        p=list(p)
        p=sorted(p)
        for j in range(len(p)-1):
            print(p[j],end=' ')
        print(p[-1])
    else:
        print('unique')
except:
    print('invalid')
