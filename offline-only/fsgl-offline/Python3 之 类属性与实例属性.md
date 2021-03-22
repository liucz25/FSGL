# [Python3 之 类属性与实例属性](https://www.cnblogs.com/gengyufei/p/11370026.html)

## 1、类属性与实例属性

　　类属性就相当与**全局变量**，实例对象**共有的属性**，**实例对象的属性为实例对象自己私有**。

　　**类属性**就是类对象（Tool）所拥有的属性，它被所有类对象的实例对象(实例方法)所共有，**在内存中只存在一个副本**，这个和C++中类的静态成员变量有点类似。对于公有的类属性，在类外可以通过类对象和实例对象访问。

## 2、实例：类属性

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
 1 class People(object):
 2     name = 'Jack'  #类属性(公有)
 3     __age = 12     #类属性（私有）
 4 
 5 p = People()    #创建实例对象
 6 
 7 print(p.name)           #通过实例对象，打印类属性：name
 8 print(People.name)      #通过类对象，打印类属性：name
 9 print(p.__age)            #错误，不能在类外通过实例对象访问私有的类属性
10 print(People.__age)        #错误，不能在类外通过类对象访问私有的类属性
11 
12 #结果如下：
13 # Jack
14 # Jack
15 # AttributeError: 'People' object has no attribute '__age'
16 # AttributeError: type object 'People' has no attribute '__age'
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

## 3、实例：实例属性（对象属性）

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
 1 class People(object):
 2     address = '山东'  # 类属性
 3     def __init__(self):
 4         self.name = 'xiaowang'  # 实例属性
 5         self.age = 20  # 实例属性
 6 
 7 p = People()    #创建实例对象
 8 p.age = 12  # 通过实例对象调用实例属性，更改实例属性值
 9 print(p.address)  # 通过实例对象调用类属性，并打印
10 print(p.name)  # 通过实例对象调用实例属性，并打印
11 print(p.age)  # 通过实例对象调用实例属性，并打印
12 
13 #结果：
14 # 山东
15 # xiaowang
16 # 12
17 
18 print(People.address)  # 通过类对象调用类属性，并打印
19 print(People.name)  # 错误（程序会报错），通过类对象调用实例属性，并打印
20 print(People.age)  # 错误（程序会报错），通过类对象调用实例属性，并打印
21 
22 #结果：
23 # 山东
24 # AttributeError: type object 'People' has no attribute 'name'
25 # AttributeError: type object 'People' has no attribute 'age'
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

## 4、通过实例（对象）去修改类属性

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
 1 class People(object):
 2     country = 'china'  # 类属性
 3 
 4 print(People.country)   #china
 5 p = People()
 6 print(p.country)    #china
 7 p.country = 'japan' 
 8 print(p.country)  # 实例属性会屏蔽掉同名的类属性：japan
 9 print(People.country)   #china
10 del p.country  # 删除实例属性
11 print(p.country)    #实例属性被删除后，再调用同名称的属性，会调用类属性：china
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

## 小结：

　　如果需要在**类外修改`类属性`**，**必须通过`类对象`去引用然后进行修改**。如果通过实例对象去引用，会产生一个同名的`实例属性`，这种方式修改的是`实例属性`，不会影响到`类属性`，并且之后如果通过实例对象去引用该名称的属性，**实例属性会强制屏蔽掉类属性**，即引用的是`实例属性`，除非删除了该`实例属性`。







# [谨慎修改Python的类属性](https://www.cnblogs.com/blackmatrix/p/5614327.html)

Python的类和类实例都是可变对象，可以随时给属性赋值，并且在原处修改。

在对类属性进行修改时需要特别小心，因为所有的类实例都继承共享类属性，除非实例本身存在和类属性同名的属性。对类属性进行修改，会影响到所有由这个类生成的实例。

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
class CA(object):

    cls_pre = 'aaaaa'

    def __init__(self):
        self.obj_pre = 'bbbbb'

a = CA()
b = CA()

print(a.cls_pre, a.obj_pre)
print(b.cls_pre, b.obj_pre)

CA.cls_pre = 'ccccc'
c = CA()

d = CA()
d.cls_pre = 'ddddd'

print(a.cls_pre, a.obj_pre)
print(b.cls_pre, b.obj_pre)
print(c.cls_pre, c.obj_pre)
print(d.cls_pre, d.obj_pre)
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

运行结果：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
aaaaa bbbbb
aaaaa bbbbb
ccccc bbbbb
ccccc bbbbb
ccccc bbbbb
ddddd bbbbb
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

代码中，将类属性CA.cls_pre 重新赋值为 'ccccc'。在修改类属性之后，不仅是后续创建的类实例c的cls_pre发生变化，在修改类属性之前的创建的类实例a、b的类属性cls_pre都发生了变化。

所以，当在class语句外修改类属性时，会导致所有由这个类创建的实例的类属性都随之变化，因为所有的实例都共享类属性CA.cls_pre。除非实例本身有同名的实例属性对类属性进行了覆盖，比如代码中的d.cls_pre = 'ddddd'。

 







如果是person 类 类属性可以视为count 在init中 可见把类属性加一，实现计数，类属性可以为奖金，实现自动计算总奖金