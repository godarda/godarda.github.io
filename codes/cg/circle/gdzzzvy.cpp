// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to draw a circle using the arc function
// File Name      : gdzzzvy.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <graphics.h>
int main()
{
    int gd = 0, gm = 9;
    initgraph(&gd, &gm, NULL);
    arc(100, 100, 0, 360, 50);
    delay(2000);
    return 0;
}
