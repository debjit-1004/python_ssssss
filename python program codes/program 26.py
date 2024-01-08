def s(a):
    print('area=',a*a)
    print('perimeter=',4*a)
def r(l,b):
    print('area=',l*b)
    print('perimter=',2*(l+b))
def cl(r):
    print('area=',math.pi*r*r)
    print('perimter=',math.pi*2*r)
import math
c=int(input('enter 1 fpr square, 2 for rectangle,3 for circle'))
if c==1:
    a1=float(input('enter side length'))
    s(a1)
elif c==2:
    a2,a3=eval(input('enter length and breadth'))
    r(a2,a3)
else:
    a4=float(input('enter the radius'))
    cl(a4)
