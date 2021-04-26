from tkinter import *

class Application(Frame):
    def say_hi(self):
        print ("hi there, everyone!")

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})




    def label_click(self):
        self.pack_forget();
        self.entry=Entry();
        self.entry.pack();

        print("label clicked")

    def mytable(self):

        self.label = Button(self)
        self.label["text"] = "label"
        self.label["fg"]   = "green"
        self.label["command"] =  self.label_click

        self.label.pack()



    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        # self.createWidgets()
        self.mytable()

root = Tk()
app = Application(master=root)
app.mainloop()
# root.destroy()
