#find the greatest number from n numbers
def g(a,b):
    if a>b:
        return a
    else:
        return b
n=int(input('no. of items:'))
a1=float(input('enter first number'))
for i in range(n-1):
    a2=float(input('enter number:\n'))
    a1=g(a1,a2)
print('greatest is :',a1)
