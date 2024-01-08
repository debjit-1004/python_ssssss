#program to check how many numbers less than 2021 inclusive have more 1's than 0 iun their binary form


a=0
for y in range(1,11):
    x=int(bin(y)[2:])
    zero=0
    c=0
    for i in range(7):
        if x%10==1:
            c+=1
        elif x%10==0:
            c-=1
        x/=10
    if c>0:
        a+=1
        print(int(bin(y)[2:
                         ]))
print(a)
