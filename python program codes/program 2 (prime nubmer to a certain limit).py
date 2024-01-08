#prime number upto a certain limit
i=int(input("Enter the limit:\n"))
c=0
if i==1:
        print('No prime number less than or equal to 1')
        import sys
        sys.exit()
print('The prime numbers less than or equal to ',i,'are :')
for a in range(2,i+1):
    for b in range(1,a):
        if a%b==0:
            c+=1

    if(c==1):
        print(a,end=',')
    c=0
    
