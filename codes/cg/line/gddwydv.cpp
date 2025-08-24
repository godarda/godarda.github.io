// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to draw Pixels using for loop
// File Name      : gddwydv.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <graphics.h>
int main()
{
    int i;
    int n = 50, x = 50, y = 50;
    int gm = VGAMAX, gd = DETECT;
    initgraph(&gd, &gm, NULL);
    for (i = 0; i < n; i++)
    {
        x = x + 5;
        putpixel(x, y, WHITE);
    }
    delay(7000);
    return 0;
}
