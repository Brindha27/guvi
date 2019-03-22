try:
    n=input()
    n=n.split()
    i=int(n[0])
    j=int(n[1])
    if(i<=10000 and j<=10000):
        for k in range(i+1,j):
            if(k%2==0):
                continue
            else:
                print(k,end=' ')
except:
    print('invalid')
