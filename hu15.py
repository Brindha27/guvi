try:
    le=int(input())
    n=input()
    n=n.split()
    l,s,ss,m=[],[],0,0
    for i in n:
        l.append(int(i))
    ss=max(l)
    for i in range(le):
        p=max(l[i:])
        if (p==l[i]):
            s.append(str(p))
    print(' '.join(s))
    print(ss)
except:
    print('invalid')
