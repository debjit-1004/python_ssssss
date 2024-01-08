"""
*        *
**      **
***    ***
****  ****
**********

till nth row
"""
    
row=int(input('enter the number of rows'))
for i in range (row):
    for j in range (row):
        if j<=i :
            print('*',end='')  
        else:
            print(' ',end='') 
    
    for k in range (row-1,-1,-1):
        if k<=i:
            print('*',end='')
        else:
            print(' ',end='')
    print()
         