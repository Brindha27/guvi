class Cs:
    def __init__(self,n,l):
        self.n=n
        self.l=l
    def Cal(self):
        l1=self.l
        l1=l1.sort()
        if(l1==self.l):
            print('yes')
        else:
            print('no')
        
n=int(input())
m=input()
m=m.split()
l=[]
for i in m:
    l.append(int(i))
o=Cs(n,l)
o.Cal()
