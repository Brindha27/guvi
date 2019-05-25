s=int(input())
n=input()
n=n.split()
l=[]
for i in n:
	l.append(int(i))
l.sort()
print(l[1])
