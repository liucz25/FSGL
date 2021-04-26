from tkinter import *

class MyTable(Frame):

    def __init__(self, master=None,value=[[1,2],[3,4]]):
        Frame.__init__(self, master)
        self.pack()
        self.value=value

    def mytable(self):
        self.lable=[]
        for v in range(len(self.value)):
            for i in range(v):
                self.lable[i]=Label()
                self.lable[i].pack()
        print(v)


if __name__ == '__main__':
    root = Tk()
    app = MyTable(master=root)
    app.mytable()
    app.mainloop()
    # root.destroy()
