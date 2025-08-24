// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to draw a Pixel with given coordinates
// File Name      : gdfdmuv.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <graphics.h>
int main()
{
    int gd = 0, gm = 9;
    initgraph(&gd, &gm, NULL);
    putpixel(50, 50, 15);
    delay(2000);
    return 0;
}
