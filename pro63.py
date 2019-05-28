n=input()
l=[]
for i in range(len(n)):
	l.append(n[i])
r=[]
for i in range(len(l)):
	if(l[i] not in r):
		r.append(l[i])
	else:
		break
print(len(r))
