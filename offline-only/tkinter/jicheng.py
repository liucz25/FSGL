class Person:
    '''
    classdocs
    '''
    Count = 0

    def __init__(self, name, age):
        '''
        Constructor
        @param: name the name of this person
        @param: age the age of this person
        '''
        self.name = name
        self.age = age
        Person.Count += 1

    def detail(self):
        '''
         the detail infomation of this person
        '''
        print('name is ', self.name)
        print('age is ', self.age)
        print('there are ' + str(Person.Count) + " person in the class")
class Father(Person):
    def getbaby(self):
        print("father")

class son(Father):
    # def __init__(self):
    #     Father.__init__(self,"zhangsa",23)

    def getbaby2(self):
        print("son")
        super().getbaby()

if __name__ == '__main__':
    # f=Father("fa",34)
    # f.getbaby()
    s=son("w",2)
    s.getbaby()
    s.getbaby2()