import sqlite3
my_conn = sqlite3.connect('form.db')

import tkinter as tk

my_conn = sqlite3.connect('form.db')

my_w = tk.Tk()
my_w.geometry("1300x250")

r_set = my_conn.execute('''SELECT * from STUDENT''')
i = 0
for STUDENT in r_set:
    for j in range(len(STUDENT)):
        e = Entry(my_w, width=10, fg='blue')
        e.grid(row=i, column=j)
        e.insert(END, STUDENT[j])
    i = i+1
my_w.mainloop()