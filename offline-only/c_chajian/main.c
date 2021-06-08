//
// Created by liuch on 2021/5/16.
//
#include <stdio.h>
#include <dlfcn.h>
#define SHARED

#include "d_plug.h"


void disp_logo(void ){
    printf("a plug-in simple/n");
    return;
}
/*显示语法信息*/
void disp_usage( char *app_name )
{
    printf( "usage : %s [plug-in file name (*.so) ]/n", app_name );
    return;
};

int main(int argc,char *argv[]){
    int res;
    int x=5;
    int y=3;
    char *so_filename;
    void *dp;
    char *error;
    disp_logo();
    if (argc<2){
        disp_usage(argv[0]);
        return 1;
    }

    so_filename=argv[1];
    printf("use shared object file : [ %s ]/n", so_filename );
    dp=dlopen(so_filename,RTLD_LAZY);
    if(dp=NULL){
        fprintf(stderr,dlerror());
        return 2;
    }
    printf( "load plug [ %s ] successfully./n", so_filename );
    /*获取动态链接库中的 d_plug 函数地址，即获取插件的功能代码*/
    d_plug = dlsym( dp, "d_plug" );
    error = dlerror();
    /*判断是否出错，比如该“不明插件”没有这函数*/
    if ( error )
    {
        fprintf( stderr, error );
        return 3;
    }


    /*执行插件的功能*/
    d_plug( x, y, &res );
    /*显示结果*/
    printf(" the result to %d, %d : %d./n", x, y, res );

    /*卸载插件*/
    dlclose( dp );

    return 0;
}