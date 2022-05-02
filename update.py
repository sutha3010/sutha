import sqlite3
conn=sqlite3.connect('test.db')
print('Opened database successfully')
conn.execute("UPDATE employeee set salary=24000.0 where ID=1")
conn.commit()
print('Total Number of rows updated :',conn.total_changes)
cursor=conn.execute("SELECT ID,Name,Address,Salary from employeee")
for row in cursor:
    print('ID=',row[0])
    print('Name=',row[1])
    print('Address=',row[2])
    print('Salary=',row[3]),"\n"
print('operation done succesfully')
conn.close()
       
