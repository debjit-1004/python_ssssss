#prime number uasing recursion
def prime(x,y):
    if y<x:
        prime(x,y+1)
    if x%y==0:
        print('composite')
    else:
        print('prime')
prime(int(input('enter')), 2)
