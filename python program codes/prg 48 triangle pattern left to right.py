'''
*
**
***
**
*
'''

n=int(input('enter total number of rows'))
r=int((n-1)/2)
r1=(n+1)//2
for i in range(1, r1+1):
    for j in range(0,i):
        print('*', end=' ')
    print()

for k in range(r,0,-1):
    for l in range(0,k):
        print('*', end=' ')
    print()
    