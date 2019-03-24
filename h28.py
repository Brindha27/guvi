try:
    s=input()
    l=[]
    for i in range(len(s)):
        l.append(s[i])
    r=[]
    for i in l:
        if i in r:
            continue
        else:
            if(l.count(i)>1):
                r.append(i)
    if(len(r)>0):
        for i in r:
            print(i,end='')
    else:
        print(s)
except:
    print('invalid')
