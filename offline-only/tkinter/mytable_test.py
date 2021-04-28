from tkinter import *


class MyTable(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.value = [[1, 2], [1, 3], [2, 1],[400,600]]
        self.entry=[]
        self.textvar=[]
        self.cow = len(self.value) + 1         #5   4人
        self.colomn = len(self.value[0]) + 1   #3   2项目


    def t1(self):
        Label(root, text="用户名").grid(row=0)
        Label(root, text="密码").grid(row=1)
        Entry(root).grid(row=0, column=1)
        Entry(root, show="*").grid(row=1, column=1)

    def entry_init(self):
        for i in range(len(self.value) + 1):
            var = []
            text = []
            for j in range(len(self.value[0]) + 1):
                text.append(IntVar())
                var.append(Entry(root))
            self.textvar.append(text)
            self.entry.append(var)
        # print(textvar,entry)
        # return entry, textvar

    def fenpei(self,event):
        print(event)










    def entry_add(self):
        cow = self.cow
        colomn = self.colomn
        for i in range(cow):
            for j in range(colomn):
                # print(i,j)
                if i < (cow - 1) and j < (colomn - 1):
                    self.textvar[i][j].set(self.value[i][j])
                    self.entry[i][j]["textvariable"] = self.textvar[i][j]
                    self.entry[i][j].grid(row=i, column=j)
                    self.entry[i][j].bind("<KeyRelease>", self.fenpei)   #需要把是哪个单元格传入，，，或者直接更新全局计算

                elif i < (cow - 1) and j == (colomn - 1):
                    self.textvar[i][j].set("222")
                    self.entry[i][j]["textvariable"] = self.textvar[i][j]
                    self.entry[i][j]["state"] = 'disabled'
                    self.entry[i][j].grid(row=i, column=j)
                elif i == (cow - 1) and j < (colomn - 1):
                    self.textvar[i][j].set("333")
                    self.entry[i][j]["state"] = 'disabled'

                    self.entry[i][j]["textvariable"] = self.textvar[i][j]
                    self.entry[i][j].grid(row=i, column=j)
                elif i == (cow - 1) and j == (colomn - 1):
                    self.textvar[i][j].set("999")
                    self.entry[i][j]["textvariable"] = self.textvar[i][j]
                    self.entry[i][j].grid(row=i, column=j)

    def t2(self):
        self.entry_init()
        self.entry_add()


if __name__ == "__main__":
    root = Tk()
    # column 默认值是 0

    app = MyTable()
    # app.t1()
    app.t2()
    app.mainloop()


