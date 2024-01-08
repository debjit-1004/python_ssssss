#vowels and consonanats in a file
f=open(r"C:\python program\class 12.txt",'r+')
v,c=0,0
r=f.read()
for a in r:
    if a.isalpha():
        if a in ['a','e','i','o','u','A','E','I','O','U']:
            v+=1
        else:
            c+=1
print(v,c,sep='\n ' )
