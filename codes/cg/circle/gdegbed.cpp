// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to draw concentric color-filled circles
// File Name      : gdegbed.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <graphics.h>
int main()
{
    int gd = 0, gm = 9, i, color = 1;
    initgraph(&gd, &gm, NULL);
    {
        for (i = 10; i <= 200; i = i + 15)
        {
            setcolor(color++);
            pieslice(320, 240, 0, 360, i);
            delay(100);
        }
        int gd = 0, gm = 9, i, color = 1;
        for (i = 200; i >= 10; i = i - 15)
        {
            setcolor(color++);
            pieslice(320, 240, 0, 360, i);
            delay(100);
        }
    }
    delay(7000);
    return 0;
}
