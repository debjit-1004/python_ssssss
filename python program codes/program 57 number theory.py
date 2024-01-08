'''
define
f1_prime_factors(num,empty_list)= list of prime factors of x
f2_phi_coprime(x,l)= list of numbers less than x that are coprime to x
f3_factors(x,l)= list of factors of x
f4_sum_factors(x)= sum of all factors of x
f5_nth_power(x)= if its a nth power number 
f(x,n)=if x is divisible by n
f7_fibonacci(x)= lies in fibonacci sequence
f8_consecutive_composites(x)= list of x consecutive composites
f9_circle(x)= circle with radius x
f10_ngon(x,n)= n gon with a side length of x
k(x)= x parallel lines
l(x)= 
13


'''

import math
import turtle
import tkinter

t=turtle.Turtle()

num=int(input('Enter a number to perfrom all the upper activities'))

def prime_return(x):
    c=0
    for i in range(2,x):
        if x%i==0:
            return False
    if c==0:
        return True
    
def  f1_prime_factors(x):
    l=[]
    for i in range(2,x+1):
        if x%i==0 and prime_return(i):
            l.append(i)
    print('The list of primes numbers that divide ',x,'is',l)
    return l
    
def f2_phi_coprime(x):
    l=[]
    for i in range(1,x):
        if math.gcd(i,x)==1:
            l.append(i)
    print('The list of coprime numbers less than equal to ',x,'is',l)      
    return l
    
def f3_factors(x):
    f3_factors.l=[]
    for i in range(1,x+1):
        if x%i==0:
            f3_factors.l.append(i)
    print('The lsit of all factors of ',x,'is',f3_factors.l) 
    return f3_factors.l

 
def f4_sum_factors(x):
    l=f3_factors.l
    print('The sum of all the factors of',x,'is',sum(l))
     
    
def f5_nth_power(x):
    n=int(input('Enter the power you want to check on the number'))
    if x==math.pow(math.ceil(math.pow(x,1/n)),n):
        print('The number is a nth power')
    else:
        print('The number is not',n,'th power')
  
def f7_fibonacci(x):
    a=0;b=1
    while b<=x:
        if x==a or x==b:  print(x,'is in the fibonacci sequence'); return 
        b,a=b+a,b
    print(x,'Is not in fibonacci sequence')

def f8_consecutive_composites(x):
    l=list(range(math.factorial(x+1)+2,math.factorial(x+1)+x+2))
    print('one of the sequence with',x,'consecutive composites is',l)
    
def f9_circle(x):
    turtle.circle(5*x)
    turtle.exitonclick()
    
def f10_ngon(x):
    n=int(input('enter the value of n for n-gon'))
    for i in range(1,n+1):
        degree=360/n
        t.forward(x)
        t.left(degree)       
        
def __main__():
    L=[]
    f1_prime_factors(num)
    f2_phi_coprime(num)
    f3_factors(num)
    f4_sum_factors(num)
    f5_nth_power(num)
    f7_fibonacci(num)
    f8_consecutive_composites(num)
    f9_circle(num)
    f10_ngon(num)
    
    
__main__()