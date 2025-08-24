// ----------------------------------------------------------------------------------------------------
// Title          : C++ program for Midpoint circle drawing algorithm
// File Name      : gddgwwm.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <graphics.h>
#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    float d;
    int x, y, r, x1, y1, gd = 0, gm;
    cout << "Enter the x1 coordinate ";
    cin >> x1;
    cout << "Enter the y1 coordinate ";
    cin >> y1;
    cout << "Enter the radius of circle ";
    cin >> r;
    initgraph(&gd, &gm, NULL);
    x = 0;
    y = r;
    d = 1.25 - r;
    do
    {
        putpixel(y1 + x, x1 + y, 15);
        putpixel(x1 + y, y1 + x, RED);
        putpixel(x1 + y, y1 - x, GREEN);
        putpixel(y1 + x, x1 - y, YELLOW);
        putpixel(y1 - x, x1 - y, 15);
        putpixel(x1 - y, y1 - x, RED);
        putpixel(x1 - y, y1 + x, GREEN);
        putpixel(y1 - x, x1 + y, YELLOW);
        if (d <= 0)
        {
            x++;
            y = y;
            d = d + 2 * x + 1;
        }
        else
        {
            x++;
            y = y - 1;
            d = d + 2 * (x - y) + 1;
        }
    } while (x < y);
    delay(7000);
    return 0;
}
