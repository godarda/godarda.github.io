// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to draw a counter-clockwise spiral using the arc function
// File Name      : gddkwaa.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <graphics.h>
int main()
{
    int gd = 0, gm = 9, x;
    initgraph(&gd, &gm, NULL);
    for (x = 0; x <= 210; x = x + 20)
    {
        arc(300, 250, 180, 0, 10 + x);
        arc(310, 250, 0, 180, 20 + x);
    }
    delay(7000);
    return 0;
}
