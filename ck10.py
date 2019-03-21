try:
    n=int(input())
    l=[]
    r,res=0,0
    while n>0:
        r=n%10
        l.append(r)
        n=n//10
    res=len(l)
    print(res)
except:
    print('invalid')
