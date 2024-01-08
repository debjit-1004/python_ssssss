#reverse places of list of integers
l=eval(input('enter a list:\n'))
l1=[]
for i in range(len(l)):
    l1[i]=l[len(l)-i-1]
print(l1)
