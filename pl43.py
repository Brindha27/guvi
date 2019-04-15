try:
    n=input()
    n=n.split()
    s=n[0]
    ss=n[1]
    l1,l2=[],[]
    for i in range(len(s)):
        l1.append(s[i])
    for i in range(len(ss)):
        l2.append(ss[i])
    f=l2[0]
    l=len(l2)
    nl,c=[],0
    for i in range(len(l1)):
        nl.clear()
        if(l1[i]==f):
            l=l+i
            nl=nl+l1[i:l]
            if (nl==l2):
                c=1
                break
    if(c==1):
        print('yes')
    else:
        print('no')
            
except:
    print('invalid')    
