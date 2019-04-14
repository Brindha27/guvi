try:
    le=int(input())
    n=input()
    n=n.split()
    l,s,ss,m=[],[],0,0
    for i in n:
        l.append(int(i))
    ss=max(l)
    for i in range(le):
        m=max(l[i:])
        if (m==l[i]):
            s.append(str(m))
    print(' '.join(s))
    print(ss)
except:
    print('invalid')
