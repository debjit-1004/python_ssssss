#fibonacci numbers checking
x=int(input('Enter a number:\n'))
import math
x1=5*x*x+4
x2=5*x*x-4
y1=int(math.sqrt(x1))
y2=int(math.sqrt(x2))

if x1==y1*y1 or x2==y2*y2 : 
    print('It is afibonacci number')
else:
    print('It is not a fibonacci number')

    
