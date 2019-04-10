try:
    n=input()
    l=[]
    for i in range(len(n)):
        if (n[i].islower()):
            l.append(n[i].upper())
        elif (n[i].isupper()):
            l.append(n[i].lower())
        else:
            continue      
    print(''.join(l))
except:
    print('invalid')
