try:
    n=int(input())
    m=input()
    m=m.split()
    l=[]
    for i in m:
        l.append(int(i))
    for i in l:
        if(l.count(i)==1):
            print(i)
except:
    print('invalid')
