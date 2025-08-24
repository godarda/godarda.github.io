// ----------------------------------------------------------------------------------------------------
// Title          : C++ menu-driven program to draw the thick, thin, and dotted line
// File Name      : gdhvyyk.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <graphics.h>
#include <iostream>
using namespace std;
class t_thin_d
{
    int x, y, x1, x2, y1, dx, dy, y2, xinc, yinc;
    float m, step, k;

public:
    void getdata();
    void calc();
    void draw();
    void draw1();
    void draw2();
};

void t_thin_d::getdata()
{
    cout << "Enter the x1 coordinate ";
    cin >> x1;
    cout << "Enter the y1 coordinate ";
    cin >> y1;
    cout << "Enter the x2 coordinate  ";
    cin >> x2;
    cout << "Enter the y2 coordinate  ";
    cin >> y2;
}

void t_thin_d::calc()
{
    dx = x2 - x1;
    dy = y2 - y1;
    m = dy / dx;
    if (m < 1)
    {
        step = dx;
    }
    else
    {
        step = dy;
    }
    xinc = (dx / step);
    yinc = (dy / step);
}
void t_thin_d::draw()
{
    x = x1;
    y = y1;
    int gd = DETECT, gm = VGAMAX;
    initgraph(&gd, &gm, NULL);
    putpixel(x, y, 15);
    for (k = 1; k < step; k++)
    {
        x = x + xinc;
        y = y + yinc;
        putpixel(x, y, 15);
    }
}

void t_thin_d::draw1()
{
    x = x1;
    y = y1;
    int gd = DETECT, gm = VGAMAX;
    initgraph(&gd, &gm, NULL);
    putpixel(x, y, 15);
    for (k = 1; k < step; k++)
    {
        x = x + xinc + 4;
        y = y + yinc + 4;
        putpixel(x, y, 15);
    }
}

void t_thin_d::draw2()
{
    for (int j = 1; j <= 3; j++)
    {
        putpixel(x1 + j, y1, 15);
    }
    for (int i = 1; i <= step; i++)
    {
        x1 = x1 + xinc;
        y1 = y1 + yinc;
        putpixel(x1, y1, 15);
        for (int j = 1; j <= 3; j++)
        {
            putpixel(x1 + j, y1, 15);
        }
    }
}

int main()
{
    int gd = 0, gm, ch;
    t_thin_d T;
    do
    {
        cout << "———————————————————————————————————————————";
        cout << "\nC++ program for the thick, thin, dotted line";
        cout << "\n———————————————————————————————————————————";
        cout << "\n1.Thin Line";
        cout << "\n2.Dotted Line";
        cout << "\n3.Thick Line";
        cout << "\n4.Exit";
        cout << "\n———————————————————————————————————————————";
        cout << "\nEnter your choice ";
        cin >> ch;
        switch (ch)
        {
        case 1:
            T.getdata();
            initgraph(&gd, &gm, NULL);
            T.calc();
            T.draw();
            delay(5000);
            closegraph();
            break;
        case 2:
            T.getdata();
            initgraph(&gd, &gm, NULL);
            T.calc();
            T.draw1();
            delay(5000);
            closegraph();
            break;
        case 3:
            T.getdata();
            initgraph(&gd, &gm, NULL);
            T.calc();
            T.draw2();
            delay(5000);
            closegraph();
            break;
        case 4:
            exit(0);
        default:
            cout << "\nWrong Choice Entered...Please Try Again\n";
        }
    } while (ch != 4);
    return 0;
}
