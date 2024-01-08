
with open (r"C:\Users\admin\Desktop\d_mon_69.txt",'r+') as d:
    #no. of bytes
    a=d.read()
    print(a)
    print(len(a))
    l=['debjit\n','sruti\n','deeya\n']
    d.writelines(l)
    d.flush()
    print(d.read())