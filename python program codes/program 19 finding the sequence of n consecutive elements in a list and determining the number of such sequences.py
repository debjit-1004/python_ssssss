#python program to find  if a list contains n consecutive elements
string=input('Enter the elements of the list separated by a space')
list=string.split()
n=int(input('Enter the number of consecutive elements to be checked '))
c=0
d=0
x=1
p=n
for i in range(len(list)-n+1):
    while x<p:
        if list[i]==list[x]:
            c+=1
        x+=1
        
    if c==n-1:
        print('Element',i+1,'i.e.',list[i],'has a repetation of',n,'times from index',i,'to',i+n-1
              )
        d+=1
        c=0
    x=i+1
    p+=1
print(d)

    
