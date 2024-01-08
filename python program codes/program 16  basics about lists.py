string=input('Enter the elements of a list separated by a space:\n   ')
print('\n')
list1=string.split()

#print list
print('List:',list1)

#removing duplicates
list2=[]
for item in list1:
    if item not in list2:
        list2.append(item)
print('List without duplicates:',list2)


#extending a list

    #append() function
a=input('Enter the only  element:\n')
list1.append(a)
list1.append(a)
print(list1)
b=input('Enter the values of the list to be added by giving a space after each element:\n')       
b=b.split()                                                                       
list1.append(b)        #apend function adds whole list inside a list                                                       
print(list1)

    #using + operator
b=input('Enter the values of the list to be added by giving a space after each element:\n')
b=b.split()
list1+=b      # + operator adds the elements of the list inside another list
print(list1)

    #by slicing ;list1[:0]; elements are added at the fornt
b=input('Enter the values of the list to be added by giving a space after each element:\n')
b=b.split()
list1[:0]=b
print(list1)   #acts same as the + operator i.e. adds only the elements fo alist but not the whole list inside another list

   # by extend
b=input('Enter the values of the list to be added by giving a space after each element:\n')
b=b.split()
list1.extend(b)
print(list1)





















