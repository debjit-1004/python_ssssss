l=eval(input('Enter a list:\n'))
maximum=max(l
            )
i=l.index(maximum)
if i<=int(len(l)/2):
    print('first half')
else:
    print('second half')
    
