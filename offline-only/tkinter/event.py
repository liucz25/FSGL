import tkinter
from tkinter import ttk


def xFunc1(event):
    print(f"鼠标左键点击了一次坐标是:x={event.x}y={event.y}")
    win["bg"]="red"
    print(event)

def xFunc2(event):
    # print(f"鼠标左键点击了一次坐标是:x={event.x}y={event.y}")
    print(event)


win = tkinter.Tk()
win.title("Kahn Software v1")  # #窗口标题
win.geometry("600x500+200+20")  # #窗口位置500后面是字母x
'''
鼠标点击事件
<Button-1>  鼠标左键
<Button-2>   鼠标中间键（滚轮）
<Button-3>  鼠标右键
<Double-Button-1>   双击鼠标左键
<Double-Button-3>   双击鼠标右键
<Triple-Button-1>   三击鼠标左键
<Triple-Button-3>   三击鼠标右键
'''
button1 = tkinter.Button(win, text="leftmouse button")
# button1 =tkinter.Label(win, text="leftmouse button")    # #任何的小空间都可以绑定鼠标事件
button1.bind("<ButtonPress>", xFunc1)  # #给按钮控件绑定左键单击事件

win.bind("<Property>",xFunc2)
button1.pack()

win.mainloop()