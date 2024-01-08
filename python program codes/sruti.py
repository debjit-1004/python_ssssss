import mysql.connector as sruti
con = sruti.connect(
    host='localhost',
    user="root",
    password="system"
)
if con.is_connected():
    print('connection succesful')
else:
    print('connection failed')
    c=0

cur=con.cursor()
cur.execute('show databases')
print(cur.fetchall())

cur.execute('use debjit')
cur.execute('show tables')
print(cur.fetchall())

