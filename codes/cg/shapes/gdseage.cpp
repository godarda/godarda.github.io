// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to draw a wheel using the arc, pieslice, and setcolor function
// File Name      : gdseage.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <graphics.h>
int main()
{
    int gd = 0, gm = 9;
    initgraph(&gd, &gm, NULL);
    setcolor(1);
    pieslice(200, 200, 0, 20, 150);
    setcolor(5);
    pieslice(200, 200, 40, 60, 150);
    setcolor(4);
    pieslice(200, 200, 80, 100, 150);
    setcolor(14);
    pieslice(200, 200, 120, 140, 150);
    setcolor(12);
    pieslice(200, 200, 160, 180, 150);
    setcolor(1);
    pieslice(200, 200, 200, 220, 150);
    setcolor(5);
    pieslice(200, 200, 240, 260, 150);
    setcolor(4);
    pieslice(200, 200, 280, 300, 150);
    setcolor(14);
    pieslice(200, 200, 320, 340, 150);
    setcolor(15);
    arc(200, 200, 360, 0, 150);
    delay(5000);
    return 0;
}
