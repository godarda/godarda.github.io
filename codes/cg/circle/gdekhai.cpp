// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to draw concentric circles from a fixed point
// File Name      : gdekhai.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <graphics.h>
int main()
{
    int gd = 0, gm = 9, i;
    initgraph(&gd, &gm, NULL);
    for (i = 10; i <= 150; i = i + 10)
    {
        setcolor(15);
        circle(120 + i, 200, i);
        delay(200);
    }
    delay(5000);
    return 0;
}
