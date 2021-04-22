import sqlite3
my_conn = sqlite3.connect('jobs.db')

import tkinter  as tk
from tkinter import *
my_w = tk.Tk()
my_w.geometry("1300x250")
# my_conn.execute("""DELETE FROM jobs""")
r_set=my_conn.execute('''SELECT * from jobs ''');
i=2 # row value inside the loop
for JOB in r_set:
    for j in range(len(JOB)):
        e = Entry(my_w, width=10, fg='blue')
        e.grid(row=i, column=j)
        e.insert(END, JOB[j])

my_w.mainloop()