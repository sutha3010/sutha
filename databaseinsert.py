import sqlite3
conn=sqlite3.connect('test.db')
print("Opened Database Successfully")
conn.execute("Insert into company1(Id,Name,Age,Address,Salary)values(1,'Paul',32,'California',20000.00)")
conn.execute("Insert into company1(Id,Name,Age,Address,Salary)values(2,'Allen',25,'Texas',15000.00)")
conn.execute("Insert into company1(Id,Name,Age,Address,Salary)values(3,'Teddy',23,'Norway',20000.00)")
conn.commit()
print("Records created Successfully")
conn.close()
