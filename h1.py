try:
    n=int(input())
    i=input()
    i=i.split()
    l=[]
    for j in i:
        l.append(int(j))
    n=[]
    for j in l:
        if (l.count(j)>1):
            n.append(j)
    if(len(n)>0):
        n=set(n)
        n=list(n)
        n=sorted(n)
        for j in range(len(n)-1):
            print(n[j],end=' ')
        print(n[-1])
    else:
        for j in range(len(l)-1):
            print(l[j],end=' ')
        print(l[-1])
except:
    print('invalid')
