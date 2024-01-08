#array hard problems

#1; largest,smallest,average,frequency....
l=eval(input('enter the list'))
max=l[0];min=l[0];avg=0
for a in l:
    max=a if a>max else max
    min = a if a<min else min
    avg+=a/len(l)
print(max,min,avg)   


