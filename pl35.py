try:
    n=input()
    l=[]
    for i in range(len(n)):
        if (n.count(n[i])==1):
            l.append(n[i])
    for i in range(len(l)):
        if ' ' in l:
            l.remove(' ')
    print(' '.join(l))
except:
    print('invalid')
