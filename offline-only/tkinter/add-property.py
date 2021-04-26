#想用python 的@property 和 tkinter的set 实现数据变化自动刷新界面
#没有成功


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

class Add:
    def __init__(self,v1):
        self.__summer=v1

    @property
    def summer(self):
        return self.__summer

    @summer.setter
    def summer(self,value):
        print("summer:" + self.__summer + "---->" + value)
        self.__summer=value

he=IntVar()
method=Add(int1.set(2))
he.set(method.summer)

def changevalue(self):
    he.set(int1.get() + int2.get())
    c=he.get()
    my_entry3.delete(0,END)
    my_entry3.insert(0,c)
my_entry = Entry(frame, width=20,textvariable=int1)


my_entry2 = Entry(frame, width=15,textvariable=int2)
my_entry3 = Entry(frame, width=15, textvariable=he)
# my_entry.bind("<Leave>",changevalue)
# my_entry2.bind("<Leave>",changevalue)
my_entry.pack()
my_entry2.pack()
my_entry3.pack()


root.mainloop()