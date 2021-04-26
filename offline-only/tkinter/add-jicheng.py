#思路，tkinter的stringVar的双向绑定，想继承，自己添加数据变更的处理，没成功，数值变化不通过set函数


from tkinter import *
from tkinter import StringVar


class MyStringVar(StringVar):
    def set(self, value):
        print(self+"-->"+value)
        super().set(value)
        # print(self+"-->"+value)

def retrieve():
    print(my_entry.get())
    print(my_entry2.get())


root = Tk()
root.geometry("200x150")

frame = Frame(root)
frame.pack()
int1=StringVar()
int2=MyStringVar()

d=MyStringVar()

# d.set(int1.get()+int2.get())
# print(d.get())
def changevalue(self):
    # d.set(int1.get() + int2.get())
    c=d.get()
    my_entry3.delete(0,END)
    my_entry3.insert(0,c)
my_entry = Entry(frame, width=20,textvariable=int1)


my_entry2 = Entry(frame, width=15,textvariable=int2)
my_entry3 = Entry(frame, width=15,textvariable=d)
my_entry.bind("<Leave>",changevalue)
my_entry2.bind("<Leave>",changevalue)
my_entry.pack()
my_entry2.pack()
my_entry3.pack()


root.mainloop()