
from tkinter import *

class MyTable(Frame):
    def __init__(self,master="") :
        Frame.__init__(self)
        Frame.master=master
        self.value=[[1,2],[3,4],[5,6]]

    def t1(self,master=''):
        Label(root, text="用户名").grid(row=0)
        Label(root, text="密码").grid(row=1)
        Entry(root).grid(row=0, column=1)
        Entry(root, show="*").grid(row=1, column=1)
    



    def entry_init(self):
        entry = []
        textvar = []
        for i in range(len(self.value)+1):
            var = []
            text = []
            for j in range(len(self.value[0])+1):
                text.append(IntVar())
                var.append(Entry())
            textvar.append(text)
            entry.append(var)
        # print(textvar,entry)
        return entry,textvar

    def entry_add(self,entry,textvar):
        cow = len(self.value) + 1
        colomn = len(self.value[0]) + 1
        for i in range(cow):
            for j in range(colomn):
                # print(i,j)
                if i < (cow - 1) and j < (colomn - 1):
                    textvar[i][j].set(self.value[i][j])
                    entry[i][j]["textvariable"]=textvar[i][j]
                    entry[i][j].grid(row=i+1, column=j+1)

                elif i < (cow - 1) and j == (colomn - 1):
                    textvar[i][j].set("222")
                    entry[i][j]["textvariable"] = textvar[i][j]
                    entry[i][j]["state"]='disabled'
                    entry[i][j].grid(row=i+1, column=j+1)
                elif i == (cow - 1) and j < (colomn - 1):
                    textvar[i][j].set("333")
                    entry[i][j]["state"] = 'disabled'

                    entry[i][j]["textvariable"] = textvar[i][j]
                    entry[i][j].grid(row=i+1, column=j+1)
                elif i == (cow - 1) and j == (colomn - 1):
                    textvar[i][j].set("999")
                    entry[i][j]["textvariable"] = textvar[i][j]
                    entry[i][j].grid(row=i, column=j)



    def t2(self):
        entry,textvar=self.entry_init()
        self.entry_add(entry,textvar)



if __name__=="__main__":
    root = Tk()
    # column 默认值是 0

    app=MyTable()
    # app.t1()
    app.t2()
    app.mainloop()
 

