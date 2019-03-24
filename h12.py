try:
    n=input()
    n=n.split()
    s=int(n[0])
    k=int(n[1])
    m=input()
    m=m.split()
    l=[]
    for i in m:
        l.append(int(i))
    if(s==len(l) and s>=k):
        l.sort(reverse=True)
        k=k-1
        print(l[k])
except:
    print('invalid')
