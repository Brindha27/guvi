try:
    n=input()
    d={'Sunday':'yes','Monday':'no','Tuesday':'no','Wednesday':'no','Thursday':'no','Friday':'no','Saturday':'yes'}
    print(d[n])
except:
    print('invalid')
