try:
    n=input()
    n=n.split()
    l=[]
    for i in range(len(n)):
        t=int(n[i])
        l.append(t)
    print(min(l))
except:
    print('invalid')
