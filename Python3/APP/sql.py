
import sqlite3

conn = sqlite3.connect('test.db')

# conn.execute('''create table employee(employeeid int, Emp_name varchar(25), designation varchar(25), location varchar(10),salary int, dateOfJoin date);''')
# conn.execute('''ALTER TABLE employee
#   ADD age VARCHAR(10)''')
conn.execute('''insert into employee(employeeid,Emp_name,designation,location,salary,dateOfJoin,age) values ('12345','Muazam','CEO','Kashmir','10000000','2021-01-01','20');''')
conn.execute('''select * from employee''')
ans = conn.fetchall()
for i in ans:
    print(i)