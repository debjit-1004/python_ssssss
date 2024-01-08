#wap to pint the common positive divisors of two numbers
x=int(input('Enter first number'))
y=int(input('Enter the second number'))
print('The common factors are:')
for i in range(1,x+1):
    if x%i==0 and y%i==0:
        print(i,end=',')
    
        
