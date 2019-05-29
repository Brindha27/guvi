n=int(input())
l=input()
l=l.split()
r=[]
for i in l:
	r.append(int(i))
b=[]
for i in r:
	b.append(list(bin(i)))
c=[]
for i in range(len(b)):
	c.append([b[i].count('1'),r[i]])
c.sort(reverse=True)
for i in range(len(c)):
	print(c[i][1])
