// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to draw circles using for loop
// File Name      : gdmqler.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <graphics.h>
int main()
{
    int gd = 0, gm = 9, i;
    initgraph(&gd, &gm, NULL);
    for (i = 50; i <= 300; i = i + 50)
    {
        setcolor(15);
        circle(i, i, 30);
    }
    delay(5000);
    return 0;
}
