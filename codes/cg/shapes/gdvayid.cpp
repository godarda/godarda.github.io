// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to draw a left half ellipse using the ellipse function
// File Name      : gdvayid.cpp
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
    ellipse(320, 240, 90, 270, 150, 100);
    delay(5000);
    return 0;
}
