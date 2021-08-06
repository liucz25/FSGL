
#include "tcp.h"
db_data_t tcp_node={
    .id=TCP,
    .flag=INUSE,
    .Init=init_tcp_core_node,
    .SendFunction=tcp_core_send
};


static int init_tcp_core_node(db_data_pt  pdata)
{
    if ((pdata->sock_fd=socket(AF_INET,SOCK_STREAM,0))<0)
    {
        perror("secket create error !\n");
    }
    struct sockaddr_in servaddr;
    bzero(&servaddr,sizeof(servaddr));
    servaddr.sin_family=AF_INET;
    servaddr.sin_port=htons(TCP_PORT);
    if(inet_pton(AF_INET,TCP_SERVICE,&servaddr.sin_addr)<0)
        perror("inet_pton error \n");
    if(connect(pdata->sock_fd,(struct sockaddr *)&servaddr,sizeof(servaddr))<0)
        perror("connect error \n");

}


static int tcp_core_send(db_data_pt pdata, void* sendbuffer)
{
    int ret=write(pdata->sock_fd,sendbuffer,sizeof(sendbuffer));
    if(ret<0)
        perror("write error \n");
    else
        printf("Send Sucess,send length:%d\n",ret);
    return ret;
}

static void register_tcp_core_method(db_list_pt plist,void *pdata)
{
    if (plist==NULL||pdata==NULL)
    {
        errno=EINVAL;
        exit(errno);
    }
    core_list_insert_before(&plist,0,pdata);
}

void init_core_tcp(db_list_pt plist)
{
    
    register_tcp_core_method(plist,(void * )&tcp_node);
}

