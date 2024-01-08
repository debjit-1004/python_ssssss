#list element frequency
l=eval(input('enter a list:\n'))
d={}
for a in l:
    c=0
    for b in l:
        if a==b:
            c+=1
    if (a,c) not in d:
        d[a]=c
print(d)
