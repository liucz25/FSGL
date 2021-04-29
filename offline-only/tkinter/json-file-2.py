import _json

class Table(object):
    def __init__(self):
        self.table={}
        self.head={}
        self.headline = [u"张三",u"lisi"]
        self.headlie = [u"工资",u"奖金"]
        self.head['headline']=self.headline
        self.head['headlie']=self.headlie
        self.table['head']=self.head
        self.table['head']['headline'][0]="wangwu"

        self.data={}
        self.value = [[1, 2,2], [1, 1,2], [2, 3,1], [4, 0,3]]
        self.total_lie = [888, 600,89]
        self.data['value']=self.value

        self.data['total_lie']=self.total_lie
        self.table['data']=self.data


if __name__=='__main__':
    t=Table()
    t.value=[[1, 2], [1, 1], [2, 3], [4, 0]]
    print(t.table)