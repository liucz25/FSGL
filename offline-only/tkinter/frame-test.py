from tkinter import *
from myTable import MyTable

if __name__ == '__main__':
    tk=Tk()
    frm=Frame()
    frml=Frame()
    frmr=Frame()
    tb=MyTable(frm)
    lab = Label(frm, text='lable')
    labl = Label(frml, text='lablel')
    labll = Label(frml, text='lablell')
    labr = Label(frmr, text='labler')
    # lab.pack()
    labl.pack()
    labll.pack()
    # lablll.pack()
    labr.pack()
    tb.t2()
    # frm.grid(row=0,columnspan=2)
    frm.pack()
    frml.pack()
    # frml.grid(row=1)
    # frmr.pack(side=RIGHT)

    # tb.pack()
    tk.mainloop()