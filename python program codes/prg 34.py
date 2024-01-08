l=eval(input('Enter the list:\n'))
for i in range(len(l)):
    if l[i]>=10:
        l[i]=10
print(l)
