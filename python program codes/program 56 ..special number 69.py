n=1
while n>0:
    n2=n*n
    n3=n*n*n
    print(n2,n3)
    l=len(str(n2))+len(str(n3))
    s=set(str(n2) + str(n3))
    if l==10 and s==set('1234567890'):
        print('found')
        print(n)
        break
    else:
        n+=1
    
