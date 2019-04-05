try:
    n=input()
    l=len(n)
    d={'I':1,'X':10,'V':5}
    s=0
    for i in range(l):
        s=s+d[n[i]]
    print(s)
except:
    print('invalid')
