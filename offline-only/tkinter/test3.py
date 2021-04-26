
import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("sunk")
win.geometry("750x250+200+20")
# 表格
tree = ttk.Treeview(win)
tree.pack()
# 定义列
tree["columns"] = ("姓名", "身高", "体重", "年龄", "性别")

# 设置列，列还不显示
tree.column("姓名", width=100)
tree.column("身高", width=100)
tree.column("体重", width=100)
tree.column("年龄", width=100)
tree.column("性别", width=100)
# 设置表头
tree.heading("姓名", text="姓名-name")
tree.heading("身高", text="身高-height")
tree.heading("体重", text="体重-weight")
tree.heading("年龄", text="年龄-age")
tree.heading("性别", text="性别-gender")
# 添加数据
tree.insert("", 0, text="line1", values=("1", "2", "3", "4", "5"))
tree.insert("", 0, text="line2", values=("6", "7", "8", "9", "10"))
tree.insert("", 0, text="line3", values=("11", "12", "13", "14", "15"))
tree.insert("", 0, text="line4", values=("16", "17", "18", "19", "20"))

win.mainloop()
