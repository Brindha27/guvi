import math
try:
    n=int(input())
    s=int(math.sqrt(n))
    p=int(math.pow(s,2))
    if(n==p):
        print('yes')
    else:
        print('no')
except:
    print('invalid')
