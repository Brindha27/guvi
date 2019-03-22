try:
    n=int(input())
    i=n//2
    f=0
    for j in range(2,i):
        if(n%j==0):
            f=1
            break
    if(f==1):
        print('no')
    else:
        print('yes')   
except:
    print('invalid')
