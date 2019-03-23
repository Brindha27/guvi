try:
    n=input()
    n=n.split()
    i=int(n[0])
    j=int(n[1])
    l=[]
    f=0
    for a in range(i+1,j):
        for k in range(2,a):
            if(a%k==0):
                f=1
                break
        if(f==0):
             l.append(a)
        f=0
    for s in range(len(l)-1):
        print(l[s],end=' ')
    print(l[-1])
except:
    print('invalid')
