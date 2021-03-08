from tkinter import *
from tkinter import messagebox
import tkinter as tk
r = tk.Tk()
r.title('Counting Seconds')
button = tk.Button(r, text='Stop', width=25, command=r.destroy)
button.pack()
r.mainloop()


def hello():
    msg = messagebox.showinfo("GUI Event Demo", "Button Demo")


root = tk.Tk()
root.geometry("200x200")
b = tk.Button(root, text='Fire Me', command=hello)
b.place(x=50, y=50)
root.mainloop()


def hello1():
    msg = messagebox.showinfo("GUI Event Demo", t.get())


root = tk.Tk()
root.geometry("200x200")
l1 = tk.Label(root, text="Name:")
l1.grid(row=0)
t = tk.Entry(root)
t.grid(row=0, column=1)
b = tk.Button(root, text='Fire Me', command=hello1)
b.grid(row=1, columnspan=3)
root.mainloop()

master = Tk()
w = Canvas(master, width=40, height=60)
w.pack()
canvas_height = 20
canvas_width = 200
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y)
mainloop()


top = Tk()
C = Canvas(top, bg="blue", height=250, width=300)
coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill="red")
line = C.create_line(10, 10, 200, 200, fill='white')
C.pack()
top.mainloop()


def test():
    if(v1.get() == 1):
        v2.set(0)
        print("Male")
    if(v2.get() == 1):
        v1.set(0)
        print("Female")


root = Tk()
root.title('Checkbutton Demo')
v1 = IntVar()
v2 = IntVar()
cb1 = Checkbutton(root, text='Male', variable=v1,
                  onvalue=1, offvalue=0, command=test)
cb1.grid(row=0)
cb2 = Checkbutton(root, text='Female', variable=v2,
                  onvalue=1, offvalue=0, command=test)
cb2.grid(row=1)
root.mainloop()


def choice():
    if(radio.get() == 1):
        root.configure(background='red')
    elif(radio.get() == 2):
        root.configure(background='blue')
    elif(radio.get() == 3):
        root.configure(background='green')


root = Tk()
root.geometry("200x200")
radio = IntVar()
rb1 = Radiobutton(root, text='Red', variable=radio,
                  width=25, value=1, command=choice)
rb1.grid(row=0)
rb2 = Radiobutton(root, text='Blue', variable=radio,
                  width=25, value=2, command=choice)
rb2.grid(row=1)
rb3 = Radiobutton(root, text='Green', variable=radio,
                  width=25, value=3, command=choice)
rb3.grid(row=3)
root.mainloop()

root = Tk()
root.title('Scale Demo')
root.geometry("200x200")


def slide():
    msg = messagebox.showinfo("GUI Event Demo", v.get())


v = DoubleVar()
scale = Scale(root, variable=v, from_=1, to=50, orient=HORIZONTAL)
scale.pack(anchor=CENTER)
btn = Button(root, text="Value", command=slide)
btn.pack(anchor=CENTER)
root.mainloop()
