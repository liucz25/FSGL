from tkinter import *


def retrieve():
    print(my_entry.get())
    print(my_entry2.get())


root = Tk()
root.geometry("200x150")

frame = Frame(root)
frame.pack()
int1=IntVar()
int2=IntVar()
int1.set(9)
int2.set(8)
d=IntVar()
d.set(int1.get()+int2.get())
# print(d.get())
def changevalue(self):
    d.set(int1.get() + int2.get())
    # c=d.get()
    # my_entry3.delete(0,END)
    # my_entry3.insert(0,c)
# my_entry = Entry(frame, width=20,textvariable=int1)
my_entry=Entry(frame)
my_entry["width"]=20
my_entry["textvariable"]=int1

my_entry2 = Entry(frame, width=15,textvariable=int2)
my_entry3 = Entry(frame, width=15,textvariable=d)
my_entry.bind("<Leave>",changevalue)
my_entry2.bind("<Leave>",changevalue)
my_entry.pack()
my_entry2.pack()
my_entry3.pack()


root.mainloop()