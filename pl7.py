try:
    n=input()
    s=[]
    for i in range(0,len(n)-1,2):
        s.append(n[i+1])
        s.append(n[i])
    if (len(n)%2 != 0):
        s.append(n[-1])
    print(''.join(s))
except:
    print('invalid')
