import sqlite3
conn=sqlite3.connect('test.db')
print("Opened database successfully")
conn=sqlite3.connect('test.db')
print("Opened database successfully")
conn.execute('''create table employeee(Id int primary key not null,Name Text not null,Age int not null,Address char(50),Salary Real)''')
print("Table created successfully")
conn.close()


