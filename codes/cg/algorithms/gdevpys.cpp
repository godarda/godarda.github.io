// ----------------------------------------------------------------------------------------------------
// Title          : C++ program for Bresenham's line drawing algorithm
// File Name      : gdevpys.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <graphics.h>
#include <iostream>
using namespace std;
class Bresenham
{
private:
    int x, y, x1, y1, x2, y2;

public:
    void getdata();
    void calc();
};

void Bresenham::getdata()
{
    cout << "Enter the x1 coordinate ";
    cin >> x1;
    cout << "Enter the y1 coordinate ";
    cin >> y1;
    cout << "Enter the x2 coordinate ";
    cin >> x2;
    cout << "Enter the y2 coordinate ";
    cin >> y2;
}

void Bresenham::calc()
{
    int dx, dy, p;
    dx = abs(x2 - x1);
    dy = abs(y2 - y1);
    p = 2 * dy - dx;
    if (x1 > x2)
    {
        x = x2;
        y = y2;
        x2 = x1;
    }
    else
    {
        x = x1;
        y = y1;
    }
    putpixel(x, y, 15);
    while (x < x2)
    {
        x++;
        if (p < 0)
        {
            p += 2 * dy;
        }
        else
        {
            y++;
            p = p + (2 * dy) - (2 * dx);
        }
        delay(10);
        putpixel(x, y, 15);
    }
}

int main()
{
    int gd = DETECT, gm = 9;
    Bresenham b;
    b.getdata();
    initgraph(&gd, &gm, NULL);
    b.calc();
    delay(7000);
    return 0;
}
