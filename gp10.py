n=input()
n=n.split()
a=n[0]
b=n[1]
l1=len(a)
l2=len(b)
c=0
if(l1==l2):
    for i in range(l1):
        if(a[i]!=b[i]):
            c+=1
if(c==1):
    print('yes')
else:
    print('no')
