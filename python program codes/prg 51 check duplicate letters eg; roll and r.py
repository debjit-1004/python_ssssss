# check duplicate letters eg; roll and return true if prsent in a string
from collections import Counter
s=input('enter a string')
s1=s.split()
def method1():
    c=0
    for a in s:
        c=Counter(a)
        print((c))
        print(type(str()))
        

def method2():
    d={}
    for word in s1:
        for key in word:
           d[key]=d.get(key,0)+1
        l=d.values()
        for i in l:
            if i>1:
                return True
        d={}
        print()
        
method2()