/******************************************************************************

                  版权所有 (C), 2001-2011, 神州数码网络有限公司

 ******************************************************************************
  文 件 名   : tcp.h
  版 本 号   : 初稿
  作    者   : lcz
  生成日期   : 2021年8月3日
  最近修改   :
  功能描述   : tcp.c 的头文件
  函数列表   :
  修改历史   :
  1.日    期   : 2021年8月3日
    作    者   : lcz
    修改内容   : 创建文件

******************************************************************************/

/*----------------------------------------------*
 * 包含头文件                                   *
 *----------------------------------------------*/

/*----------------------------------------------*
 * 外部变量说明                                 *
 *----------------------------------------------*/

/*----------------------------------------------*
 * 外部函数原型说明                             *
 *----------------------------------------------*/

/*----------------------------------------------*
 * 内部函数原型说明                             *
 *----------------------------------------------*/

/*----------------------------------------------*
 * 全局变量                                     *
 *----------------------------------------------*/

/*----------------------------------------------*
 * 模块级变量                                   *
 *----------------------------------------------*/

/*----------------------------------------------*
 * 常量定义                                     *
 *----------------------------------------------*/

/*----------------------------------------------*
 * 宏定义                                       *
 *----------------------------------------------*/

#include "linklist.h"

#ifndef __TCP_H__
#define __TCP_H__



#ifdef __cplusplus
#if __cplusplus
extern "C"{
#endif
#endif /* __cplusplus */
#define TCP_PORT 8888
#define TCP_SERVICE "127.0.0.1"

extern void init_core_tcp(db_list_pt plist);
static int init_tcp_core_node(db_data_pt  pdata);
static int tcp_core_send(db_data_pt pdata, void* sendbuffer);
static void register_tcp_core_method(db_list_pt plist,void *pdata);



#ifdef __cplusplus
#if __cplusplus
}
#endif
#endif /* __cplusplus */


#endif /* __TCP_H__ */
