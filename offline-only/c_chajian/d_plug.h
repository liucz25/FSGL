/*d_plug.h*/
#ifndef __D_PLUG_H

#define __D_PLUG_H


#ifdef SHARED
int ( *d_plug )( int x, int y, int *res );
#else
int d_plug( int x, int y, int *res );
#endif

#endif