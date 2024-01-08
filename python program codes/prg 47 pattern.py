'''*
***
***
'''

n=int(input('enter the number of rowas you want to print'))
for i in range(1,n+1):
    for j in range(0,i):
        print('*', end=' ')
    print()
    