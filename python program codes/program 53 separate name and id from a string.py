# get the first_name, lasst_name, id in the seuence from text separated by any number of 0s eg: debjit00000000kundu012
# will return debjit, kundu , 12

string= input('enter the string').split('0')
for a in string:
    print(a)