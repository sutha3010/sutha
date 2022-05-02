import sqlite3
conn=sqlite3.connect('test.db')
print('Opened database successfully')
conn.execute("DELETE from employeee where id=3")
conn.commit()
print('Total Number of rows deleted :',conn.total_changes)
cursor=conn.execute("SELECT Id,Name,Address,Salary from employeee")
for row in cursor:
    print('ID=',row[0])
    print('Name=',row[1])
    print('Address=',row[2])
    print('Salary=',row[3]),"\n"
print('operation done succesfully')
conn.close()
       
