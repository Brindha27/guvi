try:
    n=input()
    l=[]
    for i in range(len(n)):
        l.append(n[i])
    c1,c2=0,0
    c1=l.count('(')
    c2=l.count(')')
    if(c1==c2):
        print('yes')
    else:
        print('no')
except:
    print('invalid')
