import sqlite3
conn=sqlite3.connect('test.db')
print("Opened Database Successfully")
cursor=conn.execute("SELECT Id,Name,Address,Salary from company1")
for row in cursor:
    print"Id=",row[0]
    print"Name=",row[1]
    print"Address=",row[2]
    print"Salary=",row[3],"\n"
print("Operation done Successfully")
conn.close()
