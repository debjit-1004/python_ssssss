a=0
b=1
n=int(input('Enyer the value of n for finding the nth fibonacci number'))
c=0
print('The nth fibonacci number is:')
for i in range(n-2):
   c=a+b
   a=b
   b=c
print(b)
