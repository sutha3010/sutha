import sqlite3
conn=sqlite3.connect('test.db')
print("Opened Database Successfully")
conn.execute("UPDATE company1 set Salary=25000.00 where Id=1")
conn.execute("UPDATE company1 set Salary=20000.00 where Id=2")
conn.commit()
print("Total number of rows Updated:",conn.total_changes)
cursor=conn.execute("SELECT Id,Name,Address,Salary from company1")
for row in cursor:
    print"Id",row[0]
    print"Name=",row[1]
    print"Address=",row[2]
    print"Salary=",row[3],"\n"
print("Operation done Successfully")
conn.close()
