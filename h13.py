try:
    n=input()
    l1=[]
    for i in range(len(n)):
        l1.append(n[i])
    l2=[]
    l=len(l1)-1
    while(l>=0):
        l2.append(l1[l])
        l=l-1
    if (l1==l2):
        print('YES')
    else:
        print('NO')
except:
    print('invalid')
