// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to draw a square using the rectangle function
// File Name      : gdgyigw.cpp
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
    rectangle(50, 50, 200, 200);
    delay(5000);
    return 0;
}
