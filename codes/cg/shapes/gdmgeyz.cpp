// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to draw a convex polygon with programmable edges
// File Name      : gdmgeyz.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <graphics.h>
#include <iostream>
using namespace std;
class line
{
protected:
    int x1, x2, y1, y2;

public:
    void drawl()
    {
        float x, y, dx, dy, step;
        int i;
        dx = abs(x2 - x1);
        dy = abs(y2 - y1);
        if (dx >= dy)
        {
            step = dx;
        }
        else
            step = dy;
        dx = (x2 - x1) / step;
        dy = (y2 - y1) / step;
        x = x1 + 0.5;
        y = y1 + 0.5;
        i = 1;
        while (i <= step)
        {
            putpixel(x, y, 15);
            x = x + dx;
            y = y + dy;
            i = i + 1;
        }
        putpixel(x, y, 15);
    }
};

class polygon : public line
{
    int a[10][2];

public:
    void setpts(int i)
    {
        int j, k;
        for (j = 0; j < i; j++)
        {
            cout << "Enter the coordinate x" << j << " ";
            cin >> a[j][0];
            cout << "Enter the coordinate y" << j << " ";
            cin >> a[j][1];
        }
    }
    void drawpoly(int i)
    {
        int j;
        x1 = a[0][0];
        y1 = a[0][1];
        x2 = a[1][0];
        y2 = a[1][1];
        line::drawl();
        for (j = 1; j < i - 1; j++)
        {
            x1 = a[j][0];
            y1 = a[j][1];
            x2 = a[j + 1][0];
            y2 = a[j + 1][1];
            line::drawl();
        }
        x1 = a[j][0];
        y1 = a[j][1];
        x2 = a[0][0];
        y2 = a[0][1];
        line::drawl();
    }
};

int main()
{
    int n, gd = DETECT, gm;
    cout << "Enter the number of sides of polygon ";
    cin >> n;
    polygon P;
    P.setpts(n);
    initgraph(&gd, &gm, NULL);
    P.drawpoly(n);
    delay(5000);
    return 0;
}
