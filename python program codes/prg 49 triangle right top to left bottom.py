'''
    *
   **
  ***
 ****
*****
'''

n=int(input('enter he number of rows '))
for i in range(n,0,-1):
    for j in range(0,n+1):
        if j<i :
            print(' ', end=' ')
        else:
            print('*',end=' ')
    print()