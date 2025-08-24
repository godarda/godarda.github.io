// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to draw a color-filled ellipse using the fillellipse and sector function
// File Name      : gdazarg.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <graphics.h>
int main()
{
    int gd = 0, gm = 9;
    initgraph(&gd, &gm, NULL);
    setcolor(15);
    fillellipse(150, 100, 100, 50);
    delay(5000);
    return 0;
}
