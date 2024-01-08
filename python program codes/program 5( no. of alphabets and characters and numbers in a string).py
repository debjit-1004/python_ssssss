#counts alphabets,digits,space etc.
str=input("Enter a string: \n")
upper,lower ,number,space =0,0,0,0
for i in str:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
    elif i.isnumeric():
        number+=1
    elif i.isspace():
        space+=1
alphabets=lower+upper
oth_char=len(str)-alphabets-number-space
print("Total alphabets:", alphabets )
print("Total upercase alphabets:",upper)
print("Total lowercase alphabets:",lower)
print("Total digits",number)
print("Total spaces:",space)
print("other character:", oth_char)
