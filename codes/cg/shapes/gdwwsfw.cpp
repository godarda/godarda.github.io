// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to draw a 3D square using the bar3d function
// File Name      : gdwwsfw.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <graphics.h>
int main()
{
    int gd = 0, gm = 9;
    initgraph(&gd, &gm, NULL);
    bar3d(100, 100, 250, 250, 60, 1);
    delay(5000);
    return 0;
}
