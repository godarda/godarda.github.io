// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to draw concentric circles using for loop
// File Name      : gdmgezv.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <graphics.h>
int main()
{
    int gd = 0, gm = 9, i;
    initgraph(&gd, &gm, NULL);
    for (i = 50; i <= 100; i = i + 15)
    {
        setcolor(15);
        circle(150, 150, i);
        delay(200);
    }
    delay(5000);
    return 0;
}
