import sqlite3

try:
    conn = sqlite3.connect("jobs.db")
    print("Connection established")

except Exception as err:
    print("Connection is not established", str(err))

conn.close()
