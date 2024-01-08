#to write data in csv
import csv
f=open(r"C:\python program\class 12.csv",'w')
s=csv.writer(f)
s.writerow(['Name','Class','section','roll','age'])
while True:
    i=eval(input('enter '))
    s.writerow(i)
    c=input('t to terminate')
    if c=='t':
        break
f.close()

