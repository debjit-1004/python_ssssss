# program to print the sum of the series 1+(x/1!)+(x^2/2!)+(x^3/3!)....(x^n/n!)
x=int(input('enter the value of x:\n'))
n=int(input('enter the value of n:\n'))
s=1
for i in range(1,n+1):
    import math
    s=s+pow(x,i)/math.factorial(i)
print('The sum of the series is',s)
