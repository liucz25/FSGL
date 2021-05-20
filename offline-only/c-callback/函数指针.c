// 函数指针.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include <stdio.h>

void f() {
    printf("in f();\n");
}

int b(int a) {
    printf("a\n");
    printf("%d\n",a);
    return 0;
}

struct stu {
    char* name;
    void (*pf)();//声明
    int (*pb)(int a);
    int age;
};


int main()
{
    //std::cout << "Hello World!\n";
    void (*pf)();//声明
    int (*pb)(int a);

    pf = &f;//赋值
    (*pf)();//调用
    int a = 99;
    pb = &b;
    (*pb)(a);

    struct stu stu1;
    stu1.age = 88;
    stu1.name = "stu1.name";
    printf(stu1.name);
    printf("\n");
    printf("%d\n",stu1.age);
    stu1.pb = &b;
    stu1.pb(55);
    stu1.pf = &f;
    stu1.pf();

}