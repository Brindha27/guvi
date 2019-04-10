try:
    n=input()
    l,j=[],0
    for i in range(len(n)):
        l.append(n.count(n[i])) 
    j=l.index(max(l))
    print(n[j])
except:
    print('invalid')
