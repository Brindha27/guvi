try:
    n=input()
    l=['a','e','i','o','u','A','E','I','O','U']
    r=[]
    for i in range(len(n)):
        if n[i] not in l:
            r.append(n[i])
    r=r[::-1]
    print(''.join(r))
except:
    print('invalid')
