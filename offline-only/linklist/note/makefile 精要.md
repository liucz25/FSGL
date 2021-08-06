## makefile 精要   单目录

 

### 编译原理



#### 1.预编译

gcc -E hello.c -o hello.i

展开宏定义   引入头文件

#### 2.汇编

gcc -S hello.i -o hello.s

将C语言转化为汇编代码

#### 3.编译

gcc -c hello.s -o hello.o

#### 4.链接



### 显式规则

目标target  依赖 dep  命令 注意用tab键

```makefile
target：dep
​	cmd
```

## 变量



变量定义方式如下

```makefile
OBJ =      //常量，不能修改

OBJ ：=   //先定义一个

OBJ +=   //以后可以添加
```



引用变量$(OBJ)

伪目标

.PHONY:



```makefile
.PHONY
clean:
	rm -rf *.o $(TARGET)
```







##  通配符

```makefile
% 任意一个

？ 匹配

* 所有

## 自动变量
$@  代表目标文件
$^  代表依赖文件
$<  代表第一个依赖文件

```

## 模板

```makefile
TARGET = XXX
OBJ = x.o xx.o .......
INCLUDE = -I/home/x/xxxxxx/include/     //注意I与“目录”之间无空格
DEFS = -DDEBUG -DXXXX             //注意D与debug之间无空格
CFLAGS = -g --static
CC = gcc
LIBS = -lphtead -L/home/x/xx/xxx.a   //注意l与 phtead  线程 之间无空格  同L与目录之间无空格

$(TARGET):$(OBJ)
	$(CC) $(DEFS) $(CFLAGS) $^ -o $@ $(INCLUDE) $(LIBS)
	
.PHONY:
clean:
	rm -rf *.o $(TARGET)


```

## MAKEFILE 函数

wildcard  列出指定文件

pathsubst 替换字符串

1、wildcard : 扩展通配符
2、notdir ： 去除路径
3、patsubst ：替换通配符



## 隐式规则

GCC会自动做一些事



## 发布

* 确定程序是否存在符号表

  readelf -s test-1

* 生成符号表

  objcopy --only-keep-debug test1 test1.symbol

* 生成发布程序

  objcopy --strip-debug test1 test1-release   //抹除符号表

  * strip 再次精简

    strip test1-release       //符号表完全没有，调试困难

* 使用符号表进行程序debug

  gdb -q --symbol=test-1.symbol --exec=test-release

symbol-file ./test-1.symbol



release 发布版一般需要抹除符号表

命令：objcopy --strip-debug xxx xxx.release

strip  xxx



##  最终模板



```makefile
TARGET = XXX
SRC = $(wildcard *.c)
OBJ = $(patsubst %.c ,%.o , $(SRC))
INCLUDE = -I/home/x/xxxxxx/include/     //注意I与“目录”之间无空格
DEFS = -DDEBUG -DXXXX             //注意D与debug之间无空格
CFLAGS = -g --static
CC = gcc
LIBS = -lphtead -L/home/x/xx/xxx.a   //注意l与 phtead  线程 之间无空格  同L与目录之间无空格
RELEASE =release
SYMBOL=debug    //符号表

$(TARGET):$(OBJ)
	$(CC) $(DEFS) $(CFLAGS) $^ -o $@ $(INCLUDE) $(LIBS)
	
$(RELEASE):$(TARGET)
	objcopy --strip-debug $(TARGET) $(TSRGET).release
	strip $(TARGET).release
	
$(SYMBOL):$(TARGET)
	objcopy --only-keep-debug $(TARGET) $(TARGET).symbol

	
.PHONY:
clean:
	rm -rf *.o $(TARGET) $(TARGET).release


```



使用 make

make 

make release

make debug

make clean



