try:
    n=input()
    n=n.split()
    a=[]
    for i in n:
        a.append(int(i))
    m=max(a)
    print(m)
except:
    print('invalid')
