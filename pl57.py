n=input()
n=n.split()
a=n[0]
b=n[1]
l=[]
for i in range(len(a)):
	l.append(a[i])
print(l.count(b))
