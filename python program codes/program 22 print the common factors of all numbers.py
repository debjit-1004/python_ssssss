#wap to pint the common positive divisors of infinte numbers
x=(input('Enter the  number with a space to distinguish them'))
y=(x.split())
y=list(map(int,y))
print('The common factors are:')
z=y[0]
c=0
for i in range(1,z):
    for j in range(len(y)):
        if y[j]%i==0:
            c+=1
    if c==len(y):
        print(i,end=' ; ')
    c=0
