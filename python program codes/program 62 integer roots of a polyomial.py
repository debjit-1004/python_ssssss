# program to find out the integer roots of a polynomial
import math

index=int(input("enter the highest power of the polynomial"))
print(('Enter the coefficient of the terms with sign in a array \
    in decresing  order of powers'))
a=eval(input())
l=[]
def polynomial(x):
    p= a[index]
    for i in range(index,0,-1):
        p+= math.pow(x,index)*a[index-i]
    return p
c=0
b=0
while b>=0 and c<index:
    if polynomial(b)==0:
        l.append(b)
        c+=1
    if polynomial(-b)==0:
        l.append(-b)
        c+=1
    b+=1
        
print(l)