// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to draw a quarter color-filled circle using the pieslice function
// File Name      : gdqogsw.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <graphics.h>
int main()
{
    int gd = 0, gm = 9;
    initgraph(&gd, &gm, NULL);
    pieslice(60, 60, 0, 90, 50);
    delay(2000);
    return 0;
}
