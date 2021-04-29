from tkinter import *
from jsonFile3 import Table


class MyTable(Frame):
    def __init__(self,value,total):
        Frame.__init__(self)
        self.value = value
        self.total_lie=total

        self.he_hang=[]
        self.he_lie=[0]*len(self.value[0])
        self.total_hang=[]
        self.total_one_hang=[]
        self.fpvalue=[]
        self.total_total=0

        self.entry=[]
        self.textvar=[]
        self.var_total_lie=[]
        self.var_total_one_hang=[]
        self.var_total_toal=DoubleVar()
        self.cow = len(self.value) + 1         #5   4人
        self.colomn = len(self.value[0]) + 1   #3   2项目
    def save(self):
        table=Table()
        table.value=self.value
        table.total_lie=self.total_lie
        # print(table.__dict__)
        table.save(table.__dict__)
    def loadjson(self):
        t=Table()
        table=t.loadjson()
        # print(table)
        a=Table(table)
        # print(a)
        self.value=table.value
        self.total_lie=table.total_lie

    def add_all_hang(self,value_in,value_out):#行相加
        value_out.clear()
        for i in range(len(value_in)):
            h = 0
            for v in value_in[i]:
                h+=v
            value_out.append(h)
        # print(self.he[0],self.he)

    def add_all_lie(self):
        # h = [0]*len(self.value[0])
        self.he_lie = [0] * len(self.value[0])
        for v in self.value:
            for i in range(len(v)):
                self.he_lie[i] += v[i]
        # print(self.he_lie)
    def total_add(self):
        self.total_total=0
        for v in self.total_one_hang:
            self.total_total+=v

    def entry_init(self):
        for i in range(len(self.value) + 1):
            var = []
            text = []
            for j in range(len(self.value[0]) + 1):
                text.append(IntVar())
                var.append(Entry(root))
            self.textvar.append(text)
            self.entry.append(var)

        for i in range(len(self.total_one_hang)):
            self.var_total_one_hang.append(DoubleVar())

        for i in range(len(self.total_lie)):
            self.var_total_lie.append(DoubleVar())
        # print(textvar,entry)
        # return entry, textvar


    def entry_add(self):
        cow = self.cow
        colomn = self.colomn
        for i in range(cow):
            for j in range(colomn):
                # print(i,j)
                if i < (cow - 1) and j < (colomn - 1):
                    self.textvar[i][j].set(self.value[i][j])
                    self.entry[i][j]["textvariable"] = self.textvar[i][j]
                    self.entry[i][j].grid(row=i, column=j)
                    self.entry[i][j].bind("<KeyRelease>", self.reload)  # 需要把是哪个单元格传入，，，或者直接更新全局计算

                elif i < (cow - 1) and j == (colomn - 1):
                    # pass
                    self.var_total_one_hang[i].set(format( self.total_one_hang[i],'.2f'))
                    self.entry[i][j]["textvariable"] = self.var_total_one_hang[i]
                    self.entry[i][j]["state"] = 'disabled'
                    self.entry[i][j].grid(row=i, column=j)
                elif i == (cow - 1) and j < (colomn - 1):
                    self.var_total_lie[j].set(self.total_lie[j])
                    # self.entry[i][j]["state"] = 'disabled'

                    self.entry[i][j]["textvariable"] = self.var_total_lie[j]
                    self.entry[i][j].grid(row=i, column=j)
                    self.entry[i][j].bind("<KeyRelease>", self.reload)
                elif i == (cow - 1) and j == (colomn - 1):
                    self.var_total_toal.set(format( self.total_total,'.2f'))
                    self.entry[i][j]["textvariable"] = self.var_total_toal
                    self.entry[i][j]["state"] = 'disabled'
                    self.entry[i][j].grid(row=i, column=j)

    def fenpei(self):

        self.add_all_hang(self.value,self.he_hang)
        self.add_all_lie()
        # print(self.he_hang)
        # print(self.he_lie)
        self.total_hang.clear()
        for i in range(len(self.value)):
            h = []
            for j in range(len(self.value[i])):
                # print(i,j,self.value[i][j])
                # print(self.value[i][j]/self.he_lie[j]*self.total_lie[j])
                h.append(self.value[i][j]/self.he_lie[j]*self.total_lie[j])
            # print(i,j,h)
            self.total_hang.append(h)
        # print(self.total_hang)

        self.add_all_hang(self.total_hang,self.total_one_hang)
        # print(self.total_one_hang)

    def jisuan(self,event=0):
        #大致按照entry add的方式，更新self的value等的值，然后调用分配 应该就行
        # self.textvar[i][j].set(self.value[i][j])
        #        self.value[1][1]=self.textvar[1][1].get()
        for i in range(len(self.value)):
            for j in range(len(self.value[i])):
                # print(type(self.textvar[i][j].get()))
                # print(type(self.value[i][j]))
                self.value[i][j]=self.textvar[i][j].get()
        for i in range(len(self.total_lie)):
            self.total_lie[i]=self.var_total_lie[i].get()

        # print(self.total_lie)
        # print("jisuan")
    def reload(self,event=0):
        # print(event)
        self.jisuan()
        self.fenpei()
        self.total_add()
        self.entry_init()
        self.entry_add()
        self.save()

    def t1(self):
        Label(root, text="用户名").grid(row=0)
        Label(root, text="密码").grid(row=1)
        Entry(root).grid(row=0, column=1)
        Entry(root, show="*").grid(row=1, column=1)

    def t2(self):
        self.fenpei()
        self.total_add()
        self.entry_init()
        self.entry_add()


if __name__ == "__main__":
    root = Tk()
    # column 默认值是 0
    value = [[1, 2,2], [1, 1,2], [2, 3,1], [4, 0,3]]
    total_lie = [888, 600,89]

    app = MyTable(value,total_lie)
    # app.t1()
    # app.save()
    app.loadjson()
    app.t2()
    app.reload()
    app.save()
    app.mainloop()


