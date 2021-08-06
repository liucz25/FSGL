#include "udp.h"


static db_data_t udp_node={
    .id=UDP,
    .flag=INUSE,
   // .Init=init_udp_core_node,
    //.SendFunction=udp_core_send,
};
static void register_udp_core_method(db_list_pt plist,void *pdata)
{
    if (plist==NULL||pdata==NULL)
    {
        errno=EINVAL;
        return ;
    }
    core_list_insert_before(&plist,1,pdata);
}

void init_core_udp(db_list_pt plist)
{
    register_udp_core_method(plist,(void * )&udp_node);
}

