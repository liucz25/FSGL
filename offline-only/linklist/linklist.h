/******************************************************************************

                  版权所有 (C), 2001-2011, 神州数码网络有限公司

 ******************************************************************************
  文 件 名   : linklist.h
  版 本 号   : 初稿
  作    者   : lcz
  生成日期   : 2021年8月3日
  最近修改   :
  功能描述   : linklist.c 的头文件
  函数列表   :
  修改历史   :
  1.日    期   : 2021年8月3日
    作    者   : lcz
    修改内容   : 创建文件

******************************************************************************/
#ifndef __LINKLIST_H__
#define __LINKLIST_H__


#ifdef __cplusplus
#if __cplusplus
extern "C"{
#endif
#endif /* __cplusplus */

/*----------------------------------------------*
 * 包含头文件                                   *
 *----------------------------------------------*/
#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <time.h>
#include <signal.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/time.h>
#include <netinet/in.h>
#include <arpa/inet.h>

/*----------------------------------------------*
 * 外部变量说明                                 *
 *----------------------------------------------*/
extern errno;

/*----------------------------------------------*
 * 外部函数原型说明                             *
 *----------------------------------------------*/

/*----------------------------------------------*
 * 内部函数原型说明                             *
 *----------------------------------------------*/

/*----------------------------------------------*
 * 全局变量                                     *
 *----------------------------------------------*/
typedef unsigned int u32;
typedef unsigned char u8;
typedef unsigned short u16;

/*----------------------------------------------*
 * 模块级变量                                   *
 *----------------------------------------------*/
typedef struct db_data
{
    u8 id;
    u8 flag;
    int sock_fd;
    u8 *send_buffer;
    u32 (*Init)(struct db_data *pdata);
    int (*SendFunction)(struct db_data *pdata, void *send_buffer);
} db_data_t;
typedef  db_data_t* db_data_pt;

typedef struct db_node
{
    void *data;
    struct db_node *prev;
    struct db_node *next;
} db_node_t;
typedef db_node_t* db_node_pt;

typedef struct db_list
{
    u32 limit_size;
    db_node_pt head;
    db_node_pt tail;

} db_list_t;
typedef db_list_t* db_list_pt;

/*----------------------------------------------*
 * 常量定义                                     *
 *----------------------------------------------*/

/*----------------------------------------------*
 * 宏定义                                       *
 *----------------------------------------------*/
#define HTTP 1
#define TCP 2
#define UDP 3
#define SERIAL 4
//#define UART 4
//
#define INUSE 1
#define UNUSE 0


extern int core_listLsearch(db_list_t **list_head,void * find_data,int(* compare)(void *,void * ));
extern db_list_pt core_list_create(void);
extern void core_list_cuid(db_list_t *list_head,void (*do_function)(void *));
extern int core_list_delete(db_list_t **list_head,int num);
extern int core_list_insert_after(db_list_t **list_head, int num, void *new_node_data);
extern int core_list_insert_before(db_list_t **list_head, int num, void *new_node_data);
extern int core_list_modify(db_list_t **list_head,int num,void *new_node_data);
//extern db_list_t ** core_list_show(u32 num);
static inline void* __core_list_visit(db_list_t **list_head,u32 num);


#ifdef __cplusplus
#if __cplusplus
}
#endif
#endif /* __cplusplus */


#endif /* __LINKLIST_H__ */
