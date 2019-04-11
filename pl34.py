try:
    n=input()
    l=[]
    for i in range(0,len(n),3):
        l.append(n[i])
    print(''.join(l))
except:
    print('invalid')
