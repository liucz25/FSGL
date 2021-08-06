# linux 进程及线程

## 进程 fork

int fork（）

若出错返回-1

父进程返回>0的数，该数字为子进程的ID，进程id  pid

子进程返回0

![](D:\code\gdb调试相关\蜂蜜浏览器_微信图片_20210714193436.jpg)

父子进程共享代码



# 线程

创建线程   pthread_creat()

还有pthread_join()

![](D:\code\gdb调试相关\微信图片_20210714220909.jpg)



![](D:\code\gdb调试相关\微信图片_20210714220902.jpg)

# C 语言也能创建进程   go 语言  python 等也行 语言层面的事