import math
try:
    n=input()
    n=n.split()
    b=int(n[0])
    p=int(n[1])
    r=math.pow(b,p)
    print(int(r))
except:
    print('invalid')
