try:
    n=input()
    m=input()
    n=n.split()
    l=int(n[0])
    s=int(n[1])
    m=m.split()
    r=[]
    for i in m:
        r.append(int(i))
    if s in r:
        print('Yes')
    else:
        print('No')
except:
    print('invalid')
