try:
    n=input()
    l=len(n)
    d={'I':1,'X':10,'V':5}
    s=0
    for i in range(l):
        if (n[i]=='I'):
            if((i+1)<l):
                if((n[i+1]=='V') or (n[i+1]=='X')):
                    s=s+(-(d[n[i]]))
                else:
                    s=s+d[n[i]]
            else:
                s=s+d[n[i]]
        else:
            s=s+d[n[i]]
    print(s)
except:
    print('invalid')
