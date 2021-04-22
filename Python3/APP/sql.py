import sqlite3
conn = sqlite3.connect("week4.db")
cursor = conn.cursor()
# fetch_formDetails_sql = """SELECT * FROM formDetails;"""
# cursor.execute(fetch_formDetails_sql)
# formDetails = cursor.fetchall()
# print(formDetails)
create_table_sql = """CREATE TABLE formDetails (
   first_name VARCHAR(20),
   last_name VARCHAR(30),
   email VARCHAR(50),
   education VARCHAR(20),
   address1 VARCHAR(100),
   address2 VARCHAR(100),
   country VARCHAR(30),
   phone INTEGER,
   hobbies TEXT);"""
create_table_sql2 = """CREATE TABLE previousEmployees (
   company VARCHAR(20),
   jobTitle VARCHAR(30),
   period VARCHAR(50),
   name1 VARCHAR(20),
   phone1 INTEGER,
   name2 VARCHAR(20),
   phone2 INTEGER);"""
cursor.execute(create_table_sql)
cursor.execute(create_table_sql2)

conn.commit()
conn.close()