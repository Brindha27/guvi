try:
    n=input()
    n=n.split()
    l1=[]
    for i in range(len(n)):
        l1.append(n[i][0].upper())
    l2=[]
    k=0
    for i in range(len(n)):
        j=1
        while(j<len(n[i])):
            l2.append(n[i][j])
            l1[i]=l1[i]+l2[k]
            j=j+1
            k=k+1
    sp=' '
    print(sp.join(l1))
except:
    print('invalid')
