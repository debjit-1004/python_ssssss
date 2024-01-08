#perfrect number eg 6 factors 1,2,3 except itself sum =1+2+3=6
x= int(input('Enter the number: \n'))
i=1
s=0
while(i<x):
    if x%i==0:
        s+=i
    i+=1
if s==x:
    print(x,'is perfect number')
else:
    print(x,'is not a perfect number')
    
