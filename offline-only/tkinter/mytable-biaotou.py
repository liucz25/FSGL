from tkinter import *
from pickleTools import psave,pload

class MyTable(Frame):
    def __init__(self,value,total,headlie,headhang):
        Frame.__init__(self)
        self.value = value
        self.total_lie=total
        self.headlie=headlie
        self.headhang=headhang
        self.entryWidth=10

        self.data=[]

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
        self.var_head_hang=[]
        self.var_head_lie=[]
        self.var_total_toal=DoubleVar()
        self.cow = len(self.value) + 1         #5   4人
        self.colomn = len(self.value[0]) + 1   #3   2项目

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
        for i in range(len(self.value) + 2):
            var = []
            text = []
            for j in range(len(self.value[0]) + 2):
                text.append(DoubleVar())
                var.append(Entry(root))
            self.textvar.append(text)
            self.entry.append(var)

        for i in range(len(self.total_one_hang)):
            self.var_total_one_hang.append(DoubleVar())

        for i in range(len(self.total_lie)):
            self.var_total_lie.append(DoubleVar())

        for i in range(len(self.headhang)):
            self.var_head_hang.append(StringVar())
        for i in range(len(self.headlie)):
            self.var_head_lie.append(StringVar())
        # print(textvar,entry)
        # return entry, textvar


    def entry_add(self):
        cow = self.cow+1
        colomn = self.colomn+1
        for i in range(cow):
            for j in range(colomn):
                # print(i,j)
                if i==0: #and j<=(colomn):
                    # print(i, j)
                    self.var_head_lie[j].set(self.headlie[j])
                    self.entry[i][j]["textvariable"]=self.var_head_lie[j]
                    self.entry[i][j]["width"]=self.entryWidth
                    self.entry[i][j].grid(row=i,column=j)
                    # self.entry[i][j]["state"] = 'disabled'
                    self.entry[i][j].bind("<KeyRelease>", self.reload)

                elif j==0 and i>0 and i<cow:
                    # print(i,j)
                    self.var_head_hang[i-1].set(self.headhang[i-1])
                    self.entry[i][j]["textvariable"]=self.var_head_hang[i-1]
                    self.entry[i][j]["width"]=self.entryWidth
                    self.entry[i][j].grid(row=i,column=j)
                    # self.entry[i][j]["state"] = 'disabled'
                    self.entry[i][j].bind("<KeyRelease>", self.reload)

                elif i > 0 and i < (cow - 1) and j > 0 and j < (colomn - 1):

                    self.textvar[i-1][j-1].set(format( self.value[i-1][j-1],'.0f'))
                    self.entry[i][j]["textvariable"] = self.textvar[i-1][j-1]
                    self.entry[i][j]["width"]=self.entryWidth
                    self.entry[i][j].grid(row=i, column=j)
                    self.entry[i][j].bind("<KeyRelease>", self.reload)  # 需要把是哪个单元格传入，，，或者直接更新全局计算

                elif i>0 and i < (cow - 1) and j == (colomn - 1):
                    # pass
                    self.var_total_one_hang[i-1].set(format( self.total_one_hang[i-1],'.2f'))
                    self.entry[i][j]["textvariable"] = self.var_total_one_hang[i-1]
                    self.entry[i][j]["width"] = self.entryWidth
                    self.entry[i][j]["state"] = 'disabled'
                    self.entry[i][j].grid(row=i, column=j)
                elif i == (cow - 1) and j < (colomn - 1):
                    self.var_total_lie[j-1].set(format( self.total_lie[j-1],'.2f'))
                    # self.entry[i][j]["state"] = 'disabled'

                    self.entry[i][j]["textvariable"] = self.var_total_lie[j-1]
                    self.entry[i][j]["width"] = self.entryWidth
                    self.entry[i][j].grid(row=i, column=j)
                    self.entry[i][j].bind("<KeyRelease>", self.reload)
                elif i == (cow - 1) and j == (colomn - 1):
                    self.var_total_toal.set(format( self.total_total,'.2f'))
                    self.entry[i][j]["textvariable"] = self.var_total_toal
                    self.entry[i][j]["width"] = self.entryWidth
                    self.entry[i][j]["state"] = 'disabled'
                    self.entry[i][j].grid(row=i, column=j)
        # row = len(self.value)
        # column=len(self.value[0])
        self.btnLoad = Button( text="加载", command=self.cload)
        self.btnLoad.grid(row=cow + 3, column=1)
        self.btnSave = Button( text="保存", command=self.csave)
        self.btnSave.grid(row=cow + 3, column=2)

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

    def updatevalue(self, event=0):
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
        for i in range(len(self.headhang)):
            self.headhang[i]=self.var_head_hang[i].get()
        for i in range(len(self.headlie)):
            self.headlie[i]=self.var_head_lie[i].get()

        # print(self.total_lie)
        # print("jisuan")
    def reload(self,event=0):
        # print(event)
        self.updatevalue()
        self.fenpei()
        self.total_add()
        self.entry_init()
        self.entry_add()
    def reloadfromfile(self):
        self.fenpei()
        self.total_add()
        self.entry_init()
        self.entry_add()

    def t2(self):
        self.fenpei()
        self.total_add()
        self.entry_init()
        self.entry_add()


    def csave(self):
        self.data.clear()
        self.data.append(self.value)
        self.data.append(self.total_lie)
        self.data.append(self.headhang)
        self.data.append(self.headlie)

        psave(self.data)
        data=pload()
        print(data)

    def cload(self):
        data=pload()
        # print(data)
        self.value=[]
        self.total_lie=[]
        self.headhang=[]
        self.headlie=[]
        self.value=data[0]
        self.total_lie=data[1]
        self.headhang=data[2]
        self.headlie=data[3]
        # print(self.value)
        self.reloadfromfile()

    def test(self):
        pass
        # data=pload()
        # print(data)

if __name__ == "__main__":
    root = Tk()
    # column 默认值是 0
    value = [[1, 2,2], [1, 1,2], [2, 3,1], [4, 0,3],[3,5,7]]
    total_lie = [888, 600,89]
    headlie=["姓名","项目1","项目2","项目3","总和"]
    headhang=["张三","李四","王五","赵柳","找齐","金额"]
    app = MyTable(value,total_lie,headlie,headhang)
    # app.t1()
    app.t2()
    app.test()
    app.mainloop()


