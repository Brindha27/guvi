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
        c1=nl[:le]
        c2=nl[le:]
        if (c1==c2):
            print('YES')
        else:
            print('NO')
except:
    print('invalid')
