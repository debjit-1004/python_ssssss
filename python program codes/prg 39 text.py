#each word separated by a chracter
f=open(r"C:\python program\class 12.txt",'r+')
r=f.read()
c=input('Enter the chracter to be placed between words:\n')
l=r.split(' ')
print(c.join(l))
