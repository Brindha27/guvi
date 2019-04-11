try:
    n=input()
    l=len(n)
    if ( (l % 2) == 0 ):
        print('NO')
    else:
        nl=[]
        for i in range(l):
            nl.append(n[i])
        le=l//2
        nl.remove(nl[le])
        le=int(len(nl)/2)
        c1,c2,f=[],[],0
        c1=c1+nl[:le]
        c2=c2+nl[le:]
        for i in range(len(c1)):
            if(c1[i]==c2[i]):
                f=f+1
        if(f==len(c1)):
            print('YES')
        else:
            print('NO')
except:
    print('invalid')
