// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to draw a circle using the circle function
// File Name      : gdzepyi.cpp
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
    circle(120, 100, 75);
    delay(5000);
    return 0;
}
