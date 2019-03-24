try:
    n=int(input())
    m=input()
    m=m.split()
    l=[]
    for i in m:
        l.append(int(i))
    l=l[::-1]
    for i in range(len(l)-1):
        print(l[i],end='->')
    print(l[-1])
except:
    print('invalid')
