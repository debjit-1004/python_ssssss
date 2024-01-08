list_number=[1,2,3,4,5,6,7,8,9,10,11,12]
list_month=["january","february","march","april","may","june","july","august","septembar","octobar","novembar","decembar"]
x=int(input('Enter 1 to enter month number and check month and 2 to enter month and check month number:\n '))
if x==1:
    y=int(input('Enter 1 to enter month number and check month and 2 to enter month and check month number:\n '))
    print('The month is:\n')
    for i in range(len(list_number)):
        if list_number[i]==y:
            print(list_month[i])
else:
    y=input('Enter the month name in small case:\n ')
    print('The month number is:\n')
    y=y.lower()
    y=y.strip()
    for i in range(len(list_month)):
        if list_month[i]==y:
            print(list_number[i])
    
    

        
