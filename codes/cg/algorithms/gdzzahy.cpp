// ----------------------------------------------------------------------------------------------------
// Title          : C++ program for Bresenham's circle drawing algorithm
// File Name      : gdzzahy.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <graphics.h>
#include <iostream>
using namespace std;
int main()
{
    float d;
    int x, y, x1, y1, r, gd = 0, gm;
    cout << "Enter the x1 coordinate ";
    cin >> x1;
    cout << "Enter the y1 coordinate ";
    cin >> y1;
    cout << "Enter the radius of circle ";
    cin >> r;
    initgraph(&gd, &gm, NULL);
    x = 0;
    y = r;
    d = (3 - 2) * r;
    do
    {
        putpixel(y1 + x, x1 + y, 15);
        putpixel(x1 + y, y1 + x, 15);
        putpixel(x1 + y, y1 - x, 15);
        putpixel(y1 + x, x1 - y, 15);
        putpixel(y1 - x, x1 - y, 15);
        putpixel(x1 - y, y1 - x, 15);
        putpixel(x1 - y, y1 + x, 15);
        putpixel(y1 - x, x1 + y, 15);
        if (d <= 0)
        {
            d = d + (4 * x) + 6;
        }
        else
        {
            d = d + 4 * (x - y) + 10;
            y = y - 1;
        }
        x = x + 1;
    } while (x < y);
    delay(7000);
    return 0;
}
