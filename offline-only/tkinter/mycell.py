from tkinter import *

class MyCell(Frame):

    def __init__(self, master=None,value=0):
        Frame.__init__(self, master)
        self.pack()
        self.value=value
        self.label=Button()
        self.btn=Button()
        self.entry=Entry()
        self.mytable()

    def updat(self):
        self.value=self.entry.get()
        self.label["text"] = self.value
        # self.label["command"] = self.label_click
        # self.label.pack()
        self.entry.pack_forget()
        self.btn.pack_forget()
        self.label.pack()
    def updt(self,e):
        # print(self)
        # print(e)
        self.updat()

    def label_click(self):
        self.label.pack_forget()
        self.entry.delete(0, END)
        self.entry.insert(0, self.value)
        self.entry.bind("<Return>",self.updt)
        self.btn["text"]="更新"
        self.btn["command"]=self.updat
        self.entry.pack(side=LEFT)
        self.btn.pack(side=RIGHT)


    def mytable(self):
        self.label["text"] = self.value
        self.label["fg"]   = "green"
        self.label["command"] =  self.label_click
        self.label.pack()

if __name__ == '__main__':
    root = Tk()
    app = MyCell(master=root,value=9)
    app.mainloop()
    # root.destroy()
