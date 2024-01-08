#decimal to octal

num=int(input('enter a number')))
hex_num=hex(num)
print(hex_num)


#reverse an integer
i=int(input('enter an integer'))
rev=0
while i >0:
    rev = rev* 10 + i%10
    i/=10
print(rev)


i=input('enter a number')
print(int(i.reverse()))



#fibonacci 
limit= int(input('enter a number towhich the fibonacci sequence is to be printed'))
num1=0; num2=1
print(num1)
while num2<=limit:
    print(num2)
    num2,num1=num1+num2, num2

#factorial by recursion
def fact(x):
    if x==0:
        val = 1
    else:
        val=x*fact(x-1)
    return val
        
fact(4)

