try:
    s=input()
    s=s.split()
    res=[]
    for i in s:
        a=i[::-1]
        res.append(a)
    for i in range(len(res)-1):
        print(res[i],end=' ')
    print(res[-1])
except:
    print('invalid')
