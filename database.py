import sqlite3
conn=sqlite3.connect('test.db')
print("Opened database Successfully")
conn=sqlite3.connect('test.db')
print("Opened database Successfully")
conn.execute("""create table company1(Id int primarykey not null,Name Text not null,Age int not null,Address char(50),Salary Real)""")
print("Table created Successfully")
conn.close()
