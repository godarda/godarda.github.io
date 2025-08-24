// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to draw a square using the line function
// File Name      : gdsxlqq.cpp
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
    line(50, 50, 200, 50);
    line(200, 50, 200, 200);
    line(200, 200, 50, 200);
    line(50, 200, 50, 50);
    delay(5000);
    return 0;
}
