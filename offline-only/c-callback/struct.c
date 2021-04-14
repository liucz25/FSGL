#include <stdio.h>
//返回两个数中较大的一个
int max(int a, int b){
    return a>b ? a : b;
}

struct student{
    char *name;
    int num;
    int age;
    int (*pmax) ;
}st1;

int main(){
    char *name;
    int num,age,x, y, maxval;
    //定义函数指针
    int (*pmax)(int, int) = max;  //也可以写作int (*pmax)(int a, int b)
    
    printf("Input name:");
    scanf("%s", &name);
    printf("Input num:");
    scanf("%d", &num);  
    printf("Input age:");
    scanf("%d", &age);  
    printf("Input two numbers:");
    scanf("%d %d", &x, &y);     
    
    struct student stu1={name,num,age,max};
    
     printf("%s's name is %d，age is %d，scorce is %d！\n", stu1.name, stu1.num, stu1.age, stu1.age);









    return 0;
}

【C】结构体中包含函数

yongh701 2016-12-22 17:21:37  19287  收藏 10
分类专栏： C&amp;C++ 文章标签： C语言 结构体 函数 指针 malloc
版权
在《【C】Malloc与结构体，其实就是C语言里面的new和类》（点击打开链接）提到，C语言结构体里面也可以包含函数，如同类中有方法一样，但是不能通过直接放过一个函数进去，需要通过函数指针的方式，同时，关于类的构造函数与析构函数C语言表示是没有的，需要你自己手动解决这些问题。

下面讲讲如何在C语言中的结构体包含函数。

如下的一段代码：

#include<iostream>
#include<string>
using namespace std;
class Hello{
public:
	void sayHello(string name){
		cout<<"你好，"<<name<<endl;
	}
};
int main(){
	Hello* hello=new Hello();
	hello->sayHello("a");
	return 0;
}

简单的不想再解释，就是C++关于方法的Helloworld实力代码。运行结果如下图所示：

如果需要用纯C实现上面的东西，也就是在一个Hello的结构体里面包含一个函数，你可以写成这样：

#include<stdio.h>
#include<malloc.h>
struct Hello{
	void (*sayHello)(char* name); 
};
void sayHello(char* name){
	printf("你好，%s\n",name);
}
int main(){
	struct Hello* hello=(struct Hello *)malloc(sizeof(struct Hello));
	hello->sayHello=sayHello;//这个结构体有多少个函数，就要在这个有多少个结构体内，函数指针指向函数的声明。
	hello->sayHello("a");
	return 0;
}
运行结果和上面一模一样的，但是你要注意，本来已经比较坑爹的C++变成C语言来表达，就变得更加坑，每用这个包含函数指针的结构体，一定要声明这结构体内的指针一次。就是这么坑爹。
事实上，结构体这种写法，和C++中的这种类外函数声明写法是很类似的：

#include<iostream>
#include<string>
using namespace std;
class Hello{
public:
	void sayHello(string name);
};
void Hello::sayHello(string name){
	cout<<"你好，"<<name<<endl;
}
int main(){
	Hello* hello=new Hello();
	hello->sayHello("a");
	return 0;
}

以上三个代码，运行结果自然是一样的，只是表达不同而已
————————————————
版权声明：本文为CSDN博主「yongh701」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/yongh701/article/details/53817132