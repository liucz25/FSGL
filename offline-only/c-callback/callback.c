#include <stdio.h>
#define Methed(fmt,arg...) printf("叫醒方式："fmt"\n",##arg)
//回调函数，可用于解耦，实现插件或者动态加载方法


void callback_water(void){
    Methed("泼水叫醒");
}

void callback_hit(){
    Methed("打击叫醒");
}

void wakeup_service(void (*callback)()){//传入参数很重要 ，小括号不能省  （*callback）()
     printf("<-酒店叫醒服务->");
     callback();
}

int main(){
wakeup_service(callback_water);
wakeup_service(callback_hit);
return 0;
}