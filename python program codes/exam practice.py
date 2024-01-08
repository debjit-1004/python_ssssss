x= not (1==2) and (1!=1) or (4<3)
print(x)

import math
x=math.sqrt(2)
print(x,x**2, x*x)
print(x**2==2)
print(x*x==2)

# day of year start and no. of day input to get exact day name
def day(s,k):
    a=['sunday','monday','tueday','wdnesday','thrushday','friday','saturday']
    for j in range (len(a)):
        if a[j]==s:
            a=a[j:]+a[:j]
    k=k%7 - 1
    print(a[k])

s,k ='sunday' , 5
day(s,k)


math.fabs(3)

math.fmod(-8.2,6)

sruti= 'i love you'
if 'j' in sruti:
    print('mee toooooo')
else:
    print('fk off')
print('marry me?')


keepgoing= True
x=100
while keepgoing :
    print(x)
    x=x-10
    if x<50:
        keepgoing=False
    
for i in range(1000,1,-2):
    print(i)

x='debjit'<'sruti'
print(x)
x='debjit'<'deeya'
print(x)
x='debjit'<'deblina'
print(x)
x='debjit'<'aritri'
print(x)

print('debjit'<'e')

a='sruti'
for i in a:
    print(i,end='~')

x=input('enter your name')
y=input('enter your bae name')
txt1="my name is {fname}, i am in love with {fname1}".format(fname=x,fname1=y)
print(txt1)

print('%')

print('abd'in 'abdc')
print('A'in 'abcd')

print('deeya'.upper())
print('deeya'.capitalize())
print('deeya'.isupper())
print('deeya'+'debjit'+'love')

print(ord('A'))

print('deeya is very beautiful'.find('cute'))

print('deeya i love you'.split(' '))
k='sruti i love you'
print(k)

j=k.partition('i')
print(j)


a='sruti is the best girl i have ever seen'
print(a.count('sruti',1))

#list
l=[1,2,3,4,5,6,7,8,9]
print(l)
print(l.count(11))
print(l.append(10))
print(l.pop(9))
print(l.extend([10,11]))
del l

import random
print(random.randint(1,8))
print(random.randrange(3, 20,5))


#bubble sort increasing
list=[12,44,123,66,99,1]
print('original list', list)
n=len(list)

for a in range(n):
    for j in range(0,n-a-1):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
        
print('list after sorting',list)

#bubble sort decresaing
list=[12,44,123,66,99,1]
print('original list', list)
n=len(list)

for a in range(n):
    for j in range(0,n-a-1):
        if list[j]<list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
print('list after sorting',list)


l1=[1,2,3,4,5,6,7,8,9,10]
print(l1)
l1=l1+[11,12,13,14,15]
print(l1)

print('hello qworld')
print('this is great')

for i in range(0,1000):
    print('ssruti')
    
def factorial(x):
    print(x*factorial(x-1))
factorial(7)