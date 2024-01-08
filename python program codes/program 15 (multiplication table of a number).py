#multiplication table of a number 
num=int(input('Enter the number whose multiplication table is to be printed:'))
limit=int(input('Enter the limit like for the number 3, 3*15 has a limit of 15:'))
for i in range(1,limit+1):
    print(num,'*',i,'=',num*i)
