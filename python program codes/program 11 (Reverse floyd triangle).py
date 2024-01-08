#Reverse floyd triangle
n=int(input('Enter the number of lines of floyd triangle to be printed: \n'))
value=int(n*(n+1)/2)
for i in range(n, 0,-1):
    for j in range(i,0,-1):
        print(value, end=' ')
        value-=1
    print()
