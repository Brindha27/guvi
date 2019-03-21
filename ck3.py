try:
    v=['a','e','i','o','u','A','E','O','I','U']
    n=input()
    i=ord(n)
    if (i>=65 and i<=90) or (i>=97 and i<=122):
        if n in v:
            print('Vowel')
        else:
            print('Consonant')
    else:
        print('invalid')
except:
    print('invalid')
