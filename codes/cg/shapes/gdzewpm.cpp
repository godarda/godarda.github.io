// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to draw 'S' character using the arc function
// File Name      : gdzewpm.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <graphics.h>
int main()
{
    int gd = 0, gm = 9;
    initgraph(&gd, &gm, NULL);
    arc(100, 100, 90, 360, 30);
    arc(100, 160, 270, 0, 30);
    delay(5000);
    return 0;
}
