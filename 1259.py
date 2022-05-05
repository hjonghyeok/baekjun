while 1:
    a=input()
    if a=='0':
        break
    a=list(str(a))
    b=a.copy()
    b.reverse()
    if a==b:
        print('yes')
    else:
        print('no')