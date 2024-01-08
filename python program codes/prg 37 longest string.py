#longest string in a list of strings
l=eval(input('enter:\n'))
c=0
d=''
for a in l:
    if len(a)>c:
        c=len(a)
        d=a
print(d)
