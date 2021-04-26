from tkinter import StringVar


class MyStringVar(StringVar):
    def set(self, value):
        print("chonagxie chenggong")
        super().set(value)

