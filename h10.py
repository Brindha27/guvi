try:
    s=input()
    s=s.split()
    n=int(s[0])
    m=int(s[1])
    a=input()
    a=a.split()
    s1=[]
    for i in a:
        s1.append(int(i))
    b=input()
    b=b.split()
    s2=[]
    for i in b:
        s2.append(int(i))
    f=0
    if(set(s2).issubset(s1)):
        f=1
    if(f):
        print('YES')
    else:
        print('NO')
except:
    print('invalid')
