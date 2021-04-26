from tkinter import *


def retrieve(self):
    print("click")


root = Tk()
root.geometry("200x150")

frame = Frame(root)
frame.pack()

l=Label()
l["text"]="sdaf"
l.bind("<Button-1>",retrieve)
l.pack()
root.mainloop()