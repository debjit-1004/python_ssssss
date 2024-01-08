#format a number to millions like...
num=int(input('enter a non-negative integer'))
r=str(num)[::-1]
for i in range(2,len(r),3):
        r= r[0:i]+','+r[i:]
normal=r[::-1]
print((normal))

