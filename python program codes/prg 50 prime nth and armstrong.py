'''
finding a number is prime(2 divisors), fibonacii, nth prime, armstrong(sum of each digit raised to power of no. of digits), or not
'''
x=int(input('Enter a number '))
def prime(a):
    for i in range(2,a):
        if a%i==0:
            print(x,'not a prime')
            return True
        else:
            return False


def nth_prime():
    if result== True:
        c=0 
        for j in range(2,x):
            if prime(j)==True:
                c+=1
        print(x,'is prime',c)
        return c

def fibonacci():
    a1,a2=0,1
    while a2<x:
        a1,a2=a2,(a1+a2)
    if a2==x:
        print('It is an fibonacci number')
        
    

result=prime(x)
print(result)
result1=nth_prime()


