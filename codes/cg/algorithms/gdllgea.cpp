// ----------------------------------------------------------------------------------------------------
// Title          : C++ program for DDA line drawing algorithm
// File Name      : gdllgea.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <graphics.h>
#include <iostream>
using namespace std;
class dda
{
private:
    int x1, y1, x2, y2, x, y, k;
    float xinc, yinc, step, dx, dy;

public:
    void getdata();
    void calc();
};

void dda::getdata()
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

void dda::calc()
{
    dx = x2 - x1;
    dy = y2 - y1;
    if (dx > dy)
    {
        step = dx;
    }
    else
    {
        step = dy;
    }
    xinc = dx / step;
    yinc = dy / step;
    x = x1;
    y = y1;
    putpixel(x, y, 15);
    for (k = 0; k < step; k++)
    {
        x = x + xinc;
        y = y + yinc;
        int gm, gd = DETECT;
        putpixel(x, y, 15);
    }
}

int main()
{
    int gm = VGAMAX, gd = DETECT;
    dda d;
    d.getdata();
    initgraph(&gm, &gd, NULL);
    d.calc();
    delay(10000);
    return 0;
}
