class Rect:
    def __init__(self,w,h):
        self.__area=w*h

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self,value):
        print("want to do")
        self.__area=value

if __name__ == '__main__':
    r=Rect(4,5)
    print(r.area)
    r.area=90
    print(r.area)