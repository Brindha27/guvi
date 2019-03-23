try:
    s=int(input())
    n=input()
    n=n.split()
    l=[]
    for i in n:
        t=int(i)
        l.append(t)
    r=sorted(l)
    for i in range(len(r)-1):
        print(r[i],end=' ')
    print(r[-1])
except:
    print('invalid')
