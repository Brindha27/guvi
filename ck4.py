try:
    n=input()
    i=ord(n)
    if(i>=65 and i<=90) or (i>=97 and i<=122):
        print('Alphabet')
    else:
        print('No')
except:
    print('No')
