try:
    n=int(input())
    m=input()
    m=m.split()
    l=[]
    for i in m:
        l.append(int(i))
    v=0
    if v in m:
        if(m.count(i)==len(m)):
            print(i)
    else:
        l.sort(reverse=True)
        for i in l:
            print(i,end='')
except:
    print('invalid')
