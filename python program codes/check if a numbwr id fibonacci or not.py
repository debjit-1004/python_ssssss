#check if a given number is fibonacci number or not
#logic: n is a fibonacci number if 5n^2 + 4 or/and 5n^2 - 4 are both perfect squares
import math
def IsPerfectSquare(x):
    s=int(math.sqrt(x))
    return s*s==x
def IsFibonacci(n):
    return IsPerfectSquare(5*n*n-4) or IsPerfectSquare(5*n*n +4)
m=int(input('Enter a number to check if it is fibonacci or not:\n'))
if IsFibonacci(m)==True:
    print('Yes')
else:
    print("No")
