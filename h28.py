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
            else:
                r.append(i)
    for i in r:
        print(i,end='')
except:
    print('invalid')
