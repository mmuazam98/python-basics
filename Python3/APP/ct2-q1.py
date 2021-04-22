import tkinter as tk
from tkinter import messagebox as ms
import sqlite3

# make database and users (if not exists already) table at programme start up
with sqlite3.connect('userdetails.db') as db:
    c091 = db.cursor()

c091.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL PRIMARY KEY,password TEX NOT NULL);')
db.commit()
db.close()


# main Class
class main091:
    def __init__(self, master):
        self.master = master
        self.username091 = tk.StringVar()
        self.password091 = tk.StringVar()
        self.new_user091 = tk.StringVar()
        self.new_password091 = tk.StringVar()
        # Create Widgets
        self.drawwidgets091()

    # Login Function
    def logintodb091(self):
        with sqlite3.connect('userdetails.db') as db:
            c091 = db.cursor()
        find_user091 = ('SELECT * FROM user WHERE username = ? and password = ?')
        c091.execute(find_user091, [(self.username091.get()), (self.password091.get())])
        result091 = c091.fetchall()
        if result091:
            self.logf.pack_forget()
            self.head['text'] = 'Logged In as '+self.username091.get()
            self.head['pady'] = 150
        else:
            ms.showerror('Oops!', 'Invalid username or password.')

    def new_user091(self):
        with sqlite3.connect('userdetails.db') as db:
            c091 = db.cursor()
        find_user091 = ('SELECT username FROM user WHERE username = ?')
        c091.execute(find_user091, [(self.new_user091.get())])
        if c091.fetchall():
            ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
        else:
            ms.showinfo('Success!', 'Account Created!')
            self.login091()
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c091.execute(insert, [(self.new_user091.get()), (self.new_password091.get())])
        db.commit()

        # Frame Packing Methords

    def login091(self):
        self.username091.set('')
        self.password091.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()

    def createaccount091(self):
        self.new_user091.set('')
        self.new_password091.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()

    # Draw Widgets
    def drawwidgets091(self):
        self.head = tk.Label(self.master, text='LOGIN', pady=10)
        self.head.pack()
        self.logf = tk.Frame(self.master, padx=10, pady=10)
        tk.Label(self.logf, text='Username: ').grid(row=0, column=0)
        tk.Entry(self.logf, textvariable=self.username091).grid(row=0, column=1)

        tk.Label(self.logf, text='Password: ').grid(row=1, column=0)
        tk.Entry(self.logf, textvariable=self.password091, show='*').grid(row=1, column=1)

        tk.Button(self.logf, text=' Login ', command=self.logintodb091).grid()
        tk.Button(self.logf, text=' Create Account ', command=self.createaccount091).grid(row=2, column=1)
        self.logf.pack()

        self.crf = tk.Frame(self.master, padx=10, pady=10)
        tk.Label(self.crf, text='Username: ').grid(row=0, column=0)
        tk.Entry(self.crf, textvariable=self.new_user091).grid(row=0, column=1)

        tk.Label(self.crf, text='Password: ').grid(row=1, column=0)
        tk.Entry(self.crf, textvariable=self.new_password091, show='*').grid(row=1, column=1)

        tk.Button(self.crf, text='Create Account', command=self.new_user091).grid()
        tk.Button(self.crf, text='Go to Login', command=self.login091).grid(row=2, column=1)


if __name__ == '__main__':
    # Create Object
    # and setup window
    root091 = tk.Tk()
    root091.title('Login Form')
    root091.geometry('400x350+300+300')
    main091(root091)
    root091.mainloop()
