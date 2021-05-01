#双向数据绑定试验

#用字符串封装了一下tkinter 的StringVar，实现TkString与显示组件的双向数据绑定

#应该是成功了
from tkinter import *

class TkString():
    def __init__(self):
        self._value=""
        self.vs=StringVar()
    @property
    def value(self):
        # print(self.vs.get())
        self.vs.set(self.vs.get())
        return self.vs
    @value.setter
    def value(self,val):
        # v=self.vs.get()
        self.vs.set(val)
        # print("v="+v)
        # print("value:"+self._value+"---->"+val)
        # self._value = val
        # self.vs.set(val)



if __name__ == '__main__':
    tk=Tk()
    entry=Entry()
    # vs=StringVar()
    v=TkString()
    v2=TkString()
    lable=Label()
    lable['textvariable']=v2.value
    v2.value=1

    v.value="hhh"
    v.value="jkhu"
    # print(v.value.get())
    # vs.set(v.value)
    def changev():
        # print("d")
        global v
        v.value= "999"
        # print(v)

    entry['textvariable']=v.value
    entry.pack()
    lable.pack()
    btn=Button(tk,text ="改变v", command =changev)
    btn.pack()

    def p(event):
        # global v
        # print(event)

        # v.value =v.value.get()+event.char
        # v2=v.value
        v2.value=v.value.get()+"9"
    entry.bind("<KeyRelease>",p)
    tk.mainloop()