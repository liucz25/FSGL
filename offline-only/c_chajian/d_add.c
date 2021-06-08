/*d_add.c*/
#include <stdio.h>
#include "d_plug.h"

int d_plug( int x, int y, int *res )
{
    *res = x+y;
    return 0;
};