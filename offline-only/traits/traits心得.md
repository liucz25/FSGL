# traits很好用

## 但是打包特别费劲 ##

目前电脑装的是qt5 能正常用

但是打包失败

参考：

`https://github.com/enthought/traitsui/issues/458`
`https://github.com/enthought/pyface/issues/350`



`Thanks for the above tips. They were really helpful to get it working for me on both cx_Freeze and PyInstaller.`

`For cx_Freeze, I needed to add pyface.ui.qt4 to packages, and the Pyface and Traitsui egg-info folders to include_files`
`For PyInstaller, I had to add both the library and egg-info folders for both Pyface and Traitsui to datas`
`There may be a more efficient way to add just the necessary files, but this way at least worked for me.`



### pyinstaller 打包软件，只需执行，pyinstaller t1.py  即可，t1.py同级目录出现t1.spec文件，是文本文件，打开，在data加入，



# -*- mode: python ; coding: utf-8 -*-

```python
         datas=[('%s/pyface-7.3.0-py3.8.egg-info' % packages_path, 'pyface-7.3.0-py3.8.egg-info'),
    ('%s/traitsui-7.1.1-py3.8.egg-info' % packages_path, 'traitsui-7.1.1-py3.8.egg-info'),],
         hiddenimports=[
    'importlib_metadata',
    'importlib_resources',
    'numpy',
    'pyface',
    'pyface.toolkit',
    'pyface.ui.qt',
    'pyface.ui.qt4',
    'pyface.ui.qt4.action',
    'pyface.ui.qt4.clipboard',
    'pyface.ui.qt4.code_editor',
    'pyface.ui.qt4.console',
    'pyface.ui.qt4.data_view',
    'pyface.ui.qt4.fields',
    'pyface.ui.qt4.images',
    'pyface.ui.qt4.init',
    'pyface.ui.qt4.tasks',
    'pyface.ui.qt4.tests',
    'pyface.ui.qt4.timer',
    'pyface.ui.qt4.util',
    'pyface.ui.qt4.wizard',
    'pyface.ui.qt4.workbench',
    'pywin32_system32',
    'pywintypes',
    'scipy',
    'traitsui',
    'traitsui.qt4',
    'traitsui.qt4.extra',
    'traitsui.qt4.toolkit',
    'traitsui.toolkit',
    'traitsui.ui_traits',
],
         hookspath=[],
         runtime_hooks=[],
```


应该能行，

## 我没成功，可能是qt5的原因，不想再折腾了

# cx_freeze的方法  

cx_freeze，需要在t1.py 文件同级目录新建SETUP。py ，并运行，cx——FE·     。exe  setup、py

setup。py如下

注意"packages":和 "includes":['pyface','Traitsui ','PyQt5'],

```c
`import os`
`from cx_Freeze import setup, Executable`
`import cx_Freeze.hooks`
`def hack(finder, module):`
    `return`
`cx_Freeze.hooks.load_matplotlib = hack`
`import scipy`
`import matplotlib`
`import PyQt5.Qt`

`os.environ['ETS_TOOLKIT'] = 'qt4'`
`os.environ['QT_API'] = 'pyqt5'`
`scipy_path = os.path.dirname(scipy.__file__)` 
`pyqt5_path = os.path.dirname(PyQt5.Qt.__file__)`

`build_exe_options = {"packages": ["sys", "os", "glob",'subprocess',"pyface.ui.qt4", "tvtk.vtk_module", "tvtk.pyface.ui.wx", "matplotlib.backends.backend_qt4",'pygments.lexers',`
                                  `'tvtk.pyface.ui.qt4','pyface.qt','pyface.qt.QtGui','pyface.qt.QtCore',`
                                  `'openpyxl','scipy','matplotlib','numpy','math','matplotlib','mayavi',"statistics","sympy","mplcursors","traitsui","pyface"],`
                     `"include_files": [(str(scipy_path), "scipy"), (str(pyqt5_path), "PyQt5.Qt"), (matplotlib.get_data_path(), "mpl-data")],`
                     `"includes":['pyface','Traitsui ','PyQt5'],`
```



## 亲测无效，错误不一样，但同样无法运行

# 我没成功，不想再折腾了



# tkinter很强大，

特别是bind 能给label加点击事件，**给原来不支持事件的组件添加各种事件**，等各种事件，还能给特定类型组件的全部组件添加组件，只需bind_class。bind——class 还没亲自测试。应该行
tkinter的entry  相当于输入框，支持textvar，，，textvariable=int1 属性，可以实现组件与变量的双向绑定，操作起来相当方便，同时，在变量值发生变化，只需调用变量的set（）方法，即可实现界面更新，相当的强

例如想

```python
def changevalue(self):
    d.set(int1.get() + int2.get())
    c=d.get()
    my_entry3.delete(0,END)
    my_entry3.insert(0,c)

def changevalue(self):
    d.set(int1.get() + int2.get())
     # c=d.get()

    # my_entry3.delete(0,END)

    # my_entry3.insert(0,c)
```

 

    # 
实际 后边不用写，只需

```python
 d=IntVar()
 my_entry3 = Entry(frame, width=15,textvariable=d)
```

注意INTVAR是tkinter的类型



自动更新

亲测有效

同时可以利用vue组件思路，利用tkinter 的默认组件，搭建成自己想要的组件，满足自己需求。

亲测，试验性制作一个表格的单元格，默认显示为标签，单击变成entry，可修改

```python 
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

```

好用，想继续完善，实现table及部分单元格自动计算的功能