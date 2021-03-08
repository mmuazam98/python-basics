import tkinter as tk
from tkinter import*
from tkinter.ttk import*
from tkinter import ttk

def browsefunc():
    filename = filedialog.askopenfilename()
    pathlabel.config(text=filename)

root = tk.Tk()
root.geometry('500x500')
root.title("Job application")

ttk.Label(root, text = "Job Application",font = ("bold", 40)).grid(row = 0,column=0,columnspan=3,pady=2)
ttk.Label(root, text = "Personal Information",foreground="brown",font = ("bold", 20)).grid(row = 1,column=0,pady=2,sticky=W)
ttk.Label(root, text = "Name",font = ("bold", 10)).grid(row = 2,column=0,pady=2,sticky=W)
ttk.Label(root, text = "Email",font = ("bold", 10)).grid(row = 3,column=0,pady=2,sticky=W)
ttk.Label(root, text = "Education",font = ("bold", 10)).grid(row = 4,column=0,pady=2,sticky=W)
ttk.Label(root, text = "Resume",font = ("bold", 10)).grid(row = 5,column=0,pady=2,sticky=W)
ttk.Label(root, text = "Address",font = ("bold", 10)).grid(row = 6,column=0,pady=2,sticky=W)
ttk.Label(root, text = "Phone Number",font = ("bold", 10)).grid(row = 10,column=0,pady=2,sticky=W)
ttk.Label(root, text = "What are your hobbies?",font = ("bold", 10)).grid(row = 11,column=0,pady=2,sticky=W)
ttk.Label(root, text = "Previous/Current Employment details",foreground="brown",font = ("bold", 20)).grid(row = 13,column=0,pady=2,sticky=W)
ttk.Label(root, text = "Company Name",font = ("bold", 10)).grid(row = 14,column=0,pady=2,sticky=W)
ttk.Label(root, text = "Job Title",font = ("bold", 10)).grid(row = 15,column=0,pady=2,sticky=W)
ttk.Label(root, text = "How long were you here?",font = ("bold", 10)).grid(row = 16,column=0,pady=2,sticky=W)
ttk.Label(root, text = "Reference #1",foreground="brown",font = ("bold", 10)).grid(row = 17,column=0,pady=2,sticky=W)
ttk.Label(root, text = "Name",font = ("bold", 10)).grid(row = 18,column=0,pady=2,sticky=W)
ttk.Label(root, text = "Phone",font = ("bold", 10)).grid(row = 19,column=0,pady=2,sticky=W)
ttk.Label(root, text = "Reference #2",foreground="brown",font = ("bold", 10)).grid(row = 20,column=0,pady=2,sticky=W)
ttk.Label(root, text = "Name",font = ("bold", 10)).grid(row = 21,column=0,pady=2,sticky=W)
ttk.Label(root, text = "Phone",font = ("bold", 10)).grid(row = 22,column=0,pady=2,sticky=W)
e1=tk.Entry(root,width=30)
e1.insert(0,'First name')
e2=tk.Entry(root,width=30)
e2.insert(0,'Last name')
e3=tk.Entry(root,width=60)
e3.insert(0,'user@example.com')
e4=tk.Entry(root,width=60)
e5=tk.Entry(root,width=60)
e6=tk.Entry(root,width=20)
e7=tk.Entry(root,width=20)
e8=tk.Entry(root,width=20)
e9=tk.Entry(root,width=30)
e10=tk.Entry(root,width=30)
e11=tk.Entry(root,width=180)
e12=tk.Entry(root,width=30)
e13=tk.Entry(root,width=30)
e14=tk.Entry(root,width=30)
e15=tk.Entry(root,width=30)
e16=tk.Entry(root,width=30)
e17=tk.Entry(root,width=30)
e18=tk.Entry(root,width=30)
e1.grid(row=2,column=1,pady=2,sticky=W)
e2.grid(row=2,column=2,pady=2,sticky=W)
e3.grid(row=3,column=1,columnspan=2,pady=2,sticky=W)
e4.grid(row=6,column=1,columnspan=2,pady=2,sticky=W)
e5.grid(row=7,column=1,columnspan=2,pady=2,sticky=W)
e6.grid(row=9,column=1,pady=2,sticky=W)
e7.grid(row=9,column=2,pady=2,sticky=W)
e8.grid(row=9,column=3,pady=2,sticky=W)
e9.grid(row=10,column=1,pady=2,sticky=W)
e10.grid(row=10,column=2,pady=2,sticky=W)
e11.grid(row=12,column=0,columnspan=4,pady=2,sticky=W)
e12.grid(row=14,column=1,pady=2,sticky=W)
e13.grid(row=15,column=1,pady=2,sticky=W)
e14.grid(row=16,column=1,pady=2,sticky=W)
e15.grid(row=18,column=1,pady=2,sticky=W)
e16.grid(row=19,column=1,pady=2,sticky=W)
e17.grid(row=21,column=1,pady=2,sticky=W)
e18.grid(row=22,column=1,pady=2,sticky=W)

var = tk.StringVar()
var.set('Please choose')
choose=ttk.Combobox(root,width=57,textvariable=var)
choose['values']=('12th pass','B.Tech','M.Tech','BS','MS','PhD')
choose.grid(row=4,column=1,columnspan=2,sticky=W)
choose.current()

r = tk.StringVar()
r.set('Select a Country')
choose=ttk.Combobox(root,width=57,textvariable=r)
choose['values']=('America','Russia','Germany','India','Indonesia','China','Japan')
choose.grid(row=8,column=1,columnspan=2,sticky=W)
choose.current()

btn = Button(root,width=57, text ='Choose file', command = browsefunc)
btn.grid(row=5,column=1,columnspan=2,sticky=W)
pathlabel=Label(root)
pathlabel.grid(row=5,column=1,columnspan=2,sticky=W)

Button(root, text='Apply',width=20).place(x=180,y=640)
root.mainloop()