try:
    n=int(input())
    l=[]
    for i in range(2,n+1,2):
        if((n%i)==0):
            l.append(str(i))
    print(' '.join(l))
except:
    print('invalid')
