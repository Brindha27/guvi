try:
    n=input()
    j=0
    for i in range(len(n)):
        if(ord(n[i])>=48 and ord(n[i])<=57):
            j=j+1
    if(j==len(n)):
        print('yes')
    else:
        print('no')
except:
    print('invalid')
