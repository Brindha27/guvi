n=input()
n=n.split()
a=n[0]
b=n[1]
l=[]
for i in range(len(a)):
	l.append(a[i])
for i in range(len(l)):
	if(l[i]==b):
		print(i+1)
		break
