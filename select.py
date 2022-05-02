import sqlite3
conn=sqlite3.connect('test.db')
print('opened Database successfully')
cursor=conn.execute("SELECT ID,Name,Address,Salary from employeee")
for row in cursor:
    print('ID=',row[0])
    print('Name=',row[1])
    print('Address=',row[2])
    print('Salary=',row[3]),"\n"
print('operation done succesfully')
conn.close()
       
    
