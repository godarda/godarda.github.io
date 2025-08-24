// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to draw concentric color-filled circles from a fixed point
// File Name      : gdgzswf.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <graphics.h>
int main()
{
    int gd = 0, gm = 9, i, color = 1;
    initgraph(&gd, &gm, NULL);
    for (i = 150; i >= 0; i = i - 10)
    {
        setcolor(color++);
        pieslice(200, 20 + i, 0, 360, i);
        delay(400);
    }
    delay(7000);
    return 0;
}
