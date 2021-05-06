from peewee import *
from  datetime import date

sqlite_db=SqliteDatabase("./sqlite.db")
# print(sqlite_db)

class Person(Model):
    name=CharField()
    birthday=DateField()

    class Meta:
        database=sqlite_db

if __name__ == '__main__':
    sqlite_db.connect()
    sqlite_db.create_tables([Person])
    a=Person(name="bob",birthday=date(1960,1,15))
    a.save()
