try:
    n=int(input())
    l=input()
    l=l.split()
    r=[]
    for i in l:
        r.append(int(i))
    for i in r:
        if(r.count(i)==1):
            print(i)
except:
    print('invalid')
