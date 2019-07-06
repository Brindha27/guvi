n = int(input())
l = []
for i in range(n):
	l.append(input())
s = l[0]
l.remove(s)
le = len(s)
for i in l:
	while(le>0):
		if(s in i):
			break
		le = le -1
		s = s[:le]
print(s)
