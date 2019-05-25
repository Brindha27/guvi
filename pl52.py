s=input()
s=s.split()
a=int(s[0])
b=int(s[1])
n=input()
n=n.split()
l=[]
for i in n:
	l.append(int(i))
l.sort()
b=b-1
print(l[b])
