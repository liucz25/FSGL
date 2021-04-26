from tkinter import *

class MyCell(Frame):

    def __init__(self, master=None,value=0):
        Frame.__init__(self, master)
        self.pack()
        self.value=value
        self.label=Label()
        self.btn=Button()
        self.entry=Entry()
        self.entry.bind(self,"<Up>", self.updt())
        self.mytable()

    def updat(self):
        self.value=self.entry.get()
        self.label["text"] = self.value
        self.label.bind("<Button-1>",self.label_click)# self.label.pack()
        self.entry.pack_forget()
        self.btn.pack_forget()

    def updt(self):
        print("dd")

    def label_click(self,e):
        # self.label.pack_forget()

        self.entry.insert(0, self.value)


        self.btn["text"]="更新"
        self.btn["command"]=self.updat
        self.entry.pack(side=LEFT)
        self.btn.pack(side=RIGHT)


    def mytable(self):
        self.label["text"] = self.value
        self.label["fg"]   = "green"
        self.label.bind("<Button-1>",self.label_click)
        self.label.pack()

if __name__ == '__main__':
    root = Tk()
    app = MyCell(master=root,value=9)
    app.mainloop()
    # root.destroy()
