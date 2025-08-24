// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to draw a concave polygon
// File Name      : gdlggly.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <graphics.h>
#include <iostream>
using namespace std;
class Polygon
{
    int po[1][10], edges;

public:
    Polygon()
    {
        edges = 0;
        po[1][10] = 0;
    }
    void setedge();
    void setpo(int);
    int getedata();
    int getx(int);
    int gety(int);
};

class DrawPolygon : public Polygon
{
public:
    void lines(int, int, int, int);
} p;

void DrawPolygon::lines(int x0, int y0, int xEnd, int yEnd)
{
    line(x0, y0, xEnd, yEnd);
}

void Polygon::setedge()
{
    cout << "\nEnter the number of edges of polygon ";
    cin >> edges;
}

void Polygon::setpo(int index)
{
    cout << "Enter the coordinate x" << index + 1 << " ";
    cin >> po[0][index];
    cout << "Enter the coordinate y" << index + 1 << " ";
    cin >> po[1][index];
}

int Polygon::getedata()
{
    return edges;
}

int Polygon::getx(int index)
{
    return po[0][index];
}

int Polygon::gety(int index)
{
    return po[1][index];
}

int main()
{
    p.setedge();
    Polygon();
    int ch, ch1, ch2;
    int x0, y0, xEnd, yEnd;
    int gd, gm;
    gd = DETECT;
    ch = p.getedata() - 1;
    for (int i = 0; i <= ch; i++)
    {
        p.setpo(i);
    }
    initgraph(&gd, &gm, NULL);
    for (int i = 0; i < ch; i++)
    {
        x0 = p.getx(i);
        y0 = p.gety(i);
        xEnd = p.getx(i + 1);
        yEnd = p.gety(i + 1);
        p.lines(x0, y0, xEnd, yEnd);
    }
    x0 = xEnd;
    y0 = yEnd;
    xEnd = p.getx(0);
    yEnd = p.gety(0);
    p.lines(x0, y0, xEnd, yEnd);
    delay(7000);
    return 0;
}
