import math
try:
    n=int(input())
    s=str(n)
    r=0
    for i in range(len(s)):
       r=r+(math.pow(int(s[i]),2)) 
    print(int(r))
except:
    print('invalid')
