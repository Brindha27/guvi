try:
    i=input()
    i=i.split()
    l=[]
    for n in range(len(i)):
        t=int(i[n])
        l.append(t)
    print(min(l))
except:
    print('invalid')
