try:
    n=int(input())
    r=[]
    for i in range(1,6):
        r.append(i*n)
    for i in range(len(r)-1):
        print(r[i],end=' ')
    print(r[-1])
except:
    print('invalid')
