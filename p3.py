try:
    n=int(input())
    res=0
    while (n>0):
        r=n%10
        res=(res*10)+r
        n=n//10
    print(res)
except:
    print('invalid')
