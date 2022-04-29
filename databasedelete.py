import sqlite3
conn=sqlite3.connect('test.db')
print("Opened databse Successfully")
conn.execute("DELETE from company1 where Id=3")
conn.commit()
print("Total number of rows deleted:",conn.total_changes)
cursor=conn.execute("SELECT Id,Name,Address,Salary from company1")
for row in cursor:
    print"Id=",row[0]
    print"Name=",row[1]
    print"Address=",row[2]
    print"Salary=",row[3],"\n"
print("Operation done Successfully")
conn.close()
