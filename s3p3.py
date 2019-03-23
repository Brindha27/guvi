try:
    s=int(input())
    i=input()
    i=i.split()
    le=len(i)
    if(s==le):
        l=[]
        for n in range(s):
            t=int(i[n])
            l.append(t)
        print(min(l))
except:
    print('invalid')
