import pickle
f=open(r"C:\python program\binary.dat",'wb+')
d={}
c='y'
while c=='y':
    r=int(input('enter the roll number'))
    n=input('Enter the name of the student')
    m=float(input('Enter the marks of the student'))
    d['roll''name';'marks']=[r,n,m]
    pickle.dump(d,f)
    c=input('y to continue')
f.close()
