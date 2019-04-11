try:
    n=input()
    n=n.split()
    l1=n[0]
    l2=int(n[1])
    l=[]
    for i in range(len(l1)):
        l.append(int(l1[i]))
    print(l.count(l2))
except:
    print('invalid')
