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

        self.table=Frame(root)




    def table_build(self):
        title="多项目比例分配汇总表"
        table_title = Frame(self.table)
        title_l=Label(table_title, text=title)
        title_l.pack()
        table_title.grid(row=0,columnspan=len(self.headlie))

        table_head_lie = Frame(self.table)
        thl_s=[]
        thl_e=[]
        for i in range(len(self.headlie)):
            thl_s.append(StringVar())
            thl_e.append(Entry(table_head_lie))
        for i in range(len(self.headlie)):
            thl_s[i].set(self.headlie[i])
            thl_e[i]["textvariable"]=thl_s[i]
            thl_e[i]["width"]=self.entryWidth
            thl_e[i].grid(row=0,column=i)
            thl_e[i].bind("<KeyRelease>", self.reload)
        table_head_lie.grid(row=1,columnspan=len(self.headlie))

        table_head_hang=Frame(self.table)
        thh_s=[]
        thh_e=[]
        for i in range(len(self.headhang)):
            thh_s.append(StringVar())
            thh_e.append(Entry(table_head_hang))
        for i in range(len(self.headhang)):
            thh_s[i].set(self.headhang[i])
            thh_e[i]["textvariable"]=thh_s[i]
            thh_e[i]["width"]=self.entryWidth
            thh_e[i].grid(row=i,column=0)
            thh_e[i].bind("<KeyRelease>", self.reload)
        table_head_hang.grid(row=2,column=0,rowspan=2)

        table_core=Frame(self.table)
        s = []
        e = []
        for i in range(len(self.value)):
            ss=[]
            ee=[]
            for j in range(len(self.value[0])):
                # print(i,j)
                ss.append(DoubleVar())
                ee.append(Entry(table_core))
            s.append(ss)
            e.append(ee)

        # print("++++++++++++")
        for i in range(len(self.value)):
            for j in range(len(self.value[0])):
                # print(i, j)
                s[i][j].set(format( self.value[i][j],'.0f'))
                e[i][j]["textvariable"]=s[i][j]
                e[i][j]["width"]=self.entryWidth
                e[i][j].grid(row=i,column=j)
                e[i][j].bind("<KeyRelease>", self.reload)

        # table_core.grid(row=2,column=1,columnspan=len(self.value))
        table_core.grid(row=2, column=1)

        table_total_lie=Frame(self.table)
        ttl_s = []
        ttl_e = []
        for i in range(len(self.total_lie)):
            ttl_s.append(DoubleVar())
            ttl_e.append(Entry(table_total_lie))
        for i in range(len(self.total_lie)):
            ttl_s[i].set(self.total_lie[i])
            ttl_e[i]["textvariable"] = ttl_s[i]
            ttl_e[i]["width"] = self.entryWidth
            ttl_e[i].grid(row=0, column=i)
            # ttl_e[i].bind("<KeyRelease>", self.reload)
        table_total_lie.grid(row=3, column=1,columnspan=len(self.total_lie))

        table_total_hang = Frame(self.table)
        tth_s = []
        tth_e = []
        for i in range(len(self.total_one_hang)):
            tth_s.append(DoubleVar())
            tth_e.append(Entry(table_total_hang))
        for i in range(len(self.total_one_hang)):
            tth_s[i].set(format( self.total_one_hang[i],'.2f'))
            tth_e[i]["textvariable"] = tth_s[i]
            tth_e[i]["width"] = self.entryWidth
            tth_e[i].grid(row=i, column=0)
            tth_e[i]["state"] = 'disabled'
            # ttl_e[i].bind("<KeyRelease>", self.reload)
        table_total_hang.grid(row=2, column=len(self.headlie)-1)

        table_total=Frame(self.table)
        tt_s=DoubleVar()
        tt_e=Entry(table_total)
        tt_s.set(format(self.total_total, '.2f'))
        tt_e["textvariable"] = tt_s
        tt_e["width"] = self.entryWidth
        tt_e.grid()
        tt_e["state"] = 'disabled'
        table_total.grid(row=3,column=len(self.headlie)-1)





        self.table.pack()



    def test(self):
        self.fenpei()
        self.total_add()
        self.table_build()


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

if __name__ == "__main__":
    root = Tk()
    # column 默认值是 0
    value = [[1, 2,2,1], [1, 1,2,1], [2, 3,1,1], [4, 0,3,1],[3,5,7,1]]
    total_lie = [888, 600,89,734]
    headlie=["姓名","项目1","项目2","项目3","ff","总和"]
    headhang=["张三","李四","王五","赵柳","找齐","金额"]
    app = MyTable(value,total_lie,headlie,headhang)
    # # app.t1()
    # app.t2()
    app.test()
    app.mainloop()

