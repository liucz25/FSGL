
from tkinter import *

class MyTable(Frame):
    def __init__(self) :
        Frame.__init__(self)
        self.value=[[1,2],[3,4]]

    def t1(self):
        Label(root, text="用户名").grid(row=0)
        Label(root, text="密码").grid(row=1)
        Entry(root).grid(row=0, column=1)
        Entry(root, show="*").grid(row=1, column=1)
    
    def t2(self):
        print(self.value.shape)



if __name__=="__main__":
    root = Tk()
    # column 默认值是 0

    app=MyTable()
    # app.t1()
    app.t2()
    # app.mainloop()
 

