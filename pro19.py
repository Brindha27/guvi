# your code goes here
n = int(input())
l = []
r = []
for i in range(n):
	l.append(list(map(int,input().split())))
for i in l:
	r = r + i
r.sort()
for i in range(len(r)-1):
	print(r[i],end=' ')
print(r[-1])
	
