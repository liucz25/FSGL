#include <stdio.h>
#include "linklist.h"
#include "tcp.h"
#include "udp.h"
void show(db_data_pt pdata);
//void core_show(db_list_pt plist);
void  core_inuse_send(db_data_pt pdata);
int main()
{
    db_list_pt iot_gate=core_list_create();
    init_core_tcp(iot_gate);
    //init_core_tcp(iot_gate);
    init_core_udp(iot_gate);
    //core_list_cuid(iot_gate,core_inuse_send);
    //core_list_cuid(iot_gate,core_show(iot_gate));
    core_list_cuid(iot_gate,show);//show  函数指针 不加括号**********
    core_list_delete(&iot_gate,1);
    //core_list_delete(&iot_gate,1);
    printf("执行完成!!!! \n");
        

    return 0;
}
void  core_inuse_send(db_data_pt pdata)
{
    printf("core_inuse_send\n");
    int ret=0;
    if(pdata->flag==INUSE)
    {
        pdata->Init(pdata);
        ret=pdata->SendFunction(pdata,"hello tanzhong\n");
        printf("Inuse type :%d send sucess\n",pdata->id);
	}
    printf("some /n\n");
}
void core_show(db_list_pt plist)
{
    printf("ddd\n");
    printf("core_show %d",plist->limit_size);
    //int counter=1;
    //int num=plist->limit_size;
   // printf("counter %d,num %d",counter,num);
}
void show(db_data_pt pdata)
{
    printf("show\n");
    printf("show flag ==1         %d \n",pdata->flag);
     printf("show id ===2         %d \n",pdata->id);
}
