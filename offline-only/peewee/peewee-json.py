from peewee import *
from  datetime import date,datetime
from playhouse.shortcuts import  model_to_dict
import json

sqlite_db=SqliteDatabase("./sqlite.db")

class CJsonEncoder(json.JSONEncoder):

	def default(self, obj):
		if isinstance(obj, datetime):
			return obj.strftime('%Y-%m-%d %H:%M:%S')
		elif isinstance(obj, date):
			return obj.strftime('%Y-%m-%d')
		else:
			return json.JSONEncoder.default(self, obj)
# print(sqlite_db)
# class MyModel(Model):#不好用
#
#   def __str__(self):
#     r = {}
#     for k in self._data.keys():
#       try:
#          r[k] = str(getattr(self, k))
#       except:
#          r[k] = json.dumps(getattr(self, k))
#     return str(r)

class Person(Model):
    name=CharField()
    birthday=DateField()

    class Meta:
        database=sqlite_db

if __name__ == '__main__':
    sqlite_db.connect()
    sqlite_db.create_tables([Person])
    a=Person(name="bob",birthday=date(1960,1,13))
    a.save()
    grandma = Person.get(Person.name == 'bob')
    print(model_to_dict(grandma))
    data2 = json.dumps(model_to_dict(grandma),cls=CJsonEncoder)#沒成功
    # print(data2)
    # data2 = json.dumps(grandma)
    print(data2)
