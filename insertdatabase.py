import sqlite3
conn=sqlite3.connect('test.db')
print("Opened Database successfully")
conn.execute("Insert into employeee(ID,Name,Age,Address,Salary)values(1,'Paul',32,'California',2000.00)")
conn.execute("Insert into employeee(ID,Name,Age,Address,Salary)values(2,'Allen',25,'Texas',15000.00)")
conn.execute("Insert into employeee(ID,Name,Age,Address,Salary)values(3,'Teddy',23,'Norway',10000.00)")
conn.commit()
print("Records created Successfully")
conn.close()
