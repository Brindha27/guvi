try:
    n=int(input())
    f=0
    if (n>1):    
        for j in range(2,n):
            if(n%j==0):
                f=1
                break
        if(f==1):
            print('no')
        else:
            print('yes')
    else:
        print('no')
except:
    print('invalid')
