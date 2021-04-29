import json
def loadjson():
    with open("./data.json", 'r') as f:
        table = json.load(f)
        print(table)
        head=table[0]
        print(head)

def save(data):
    with open("./data.json","w") as f:
        json.dump(data,f)
        print("ok")
if __name__ == "__main__":
    # table=[]
    # head=[]
    # headline = [u"张三",u"lisi"]
    # headlie = [u"工资",u"奖金"]
    # head.append(headline)
    # head.append(headlie)
    # data=[]
    # # column 默认值是 0
    # value = [[1, 2,2], [1, 1,2], [2, 3,1], [4, 0,3]]
    # total_lie = [888, 600,89]
    # data.append(value)
    # data.append(total_lie)
    # table.append(head)
    # table.append(data)
    # t=json.dumps(table)
    # print(table[0])
    # print(t)
    # t2=json.loads(t)
    # print(t2)
    # save(table)
    loadjson()
# json解析时报错
#
# json.load(filename)
# json.loads(string)
# 一个从文件加载，一个从内存加载
