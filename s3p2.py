try:
    s=int(input())
    n=input()
    n=n.split()
    l=[]
    le=len(n)
    if(s==le):
        for i in range(s):
            t=int(n[i])
            l.append(t)
        print(max(l))
except:
    print('invalid')
