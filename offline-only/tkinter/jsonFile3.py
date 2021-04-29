import json


class Table(object):
    def __init__(self,d=0):
        # self.headline = [u"张三",u"lisi"]
        # self.headlie = [u"工资",u"奖金"]
        # self.value = [[1, 2,2], [1, 1,2], [2, 3,1], [4, 0,3]]
        # self.total_lie = [888, 600,89]
        self.headline=[]
        print(type(d))

    def loadjson(self):
        with open("./data.json", 'r') as f:
            # table=Table()
            table =json.load(f)
            # print(type(table))
        return  table

    def save(self,data):
        with open("./data.json", "w") as f:
            json.dump(data, f)
            print(data)

if __name__=='__main__':
    t=Table()
    # t.value=[[1, 2], [1, 1], [2, 3], [4, 0]]
    # print(t)
    # t.save(t.__dict__)
    t.loadjson()