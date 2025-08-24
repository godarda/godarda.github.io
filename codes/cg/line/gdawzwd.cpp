// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to draw a dashed line using the setline function
// File Name      : gdawzwd.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <graphics.h>
int main()
{
    int gd = 0, gm = 9;
    initgraph(&gd, &gm, NULL);
    setlinestyle(DASHED_LINE, 5, NORM_WIDTH);
    setcolor(15);
    line(50, 50, 150, 150);
    delay(2000);
    return 0;
}
