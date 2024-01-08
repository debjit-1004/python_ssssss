#postive negative separate list
l=eval(input('enter a list'))
p,n=[],[]
for a in l:
    if a<0:
        p.append(a)
    else:
        n.append(a)
print(p,n,sep='\n')

