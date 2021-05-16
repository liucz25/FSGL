#include <iostream>
#include "test.h"

int g_num = 0;   ///全局变量

int Test::get() { return g_num; }
void Test::set(const int num){ g_num = num; }

#ifdef __cplusplus
extern "C" {
#endif

Test* create(){ return new Test; }

#ifdef __cplusplus
 }
#endif

