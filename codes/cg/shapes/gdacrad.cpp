// ----------------------------------------------------------------------------------------------------
// Title          : C++ menu-driven program to draw the convex polygons
// File Name      : gdacrad.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <graphics.h>
#include <iostream>
using namespace std;
class polygon
{
private:
    int x1, y1, x2, y2, x, y, k;
    float dx, dy, step, xinc, yinc;

public:
    void SRtri(int x1, int y1, int x2, int y2)
    {
        dx = x2 - x1;
        dy = y2 - y1;
        if (abs(dx) >= abs(dy))
        {
            step = abs(dx);
        }
        else
        {
            step = abs(dy);
        }
        xinc = dx / step;
        yinc = dy / step;
        x = x1;
        y = y1;
        putpixel(x, y, WHITE);
        for (k = 0; k < step; k++)
        {
            x = x + xinc;
            y = y + yinc;
            putpixel(x, y, WHITE);
        }
    }
};

int main()
{
    int x1, x2, y1, y2, ch, x3, y3;
    int gd = DETECT, gm;
    polygon p;
    do
    {
        cout << "———————————————————————————————————————————";
        cout << "\nProgram to draw the convex polygons";
        cout << "\n———————————————————————————————————————————";
        cout << "\n1.Square\n2.Rectangle\n3.Triangle\n4.Exit";
        cout << "\n———————————————————————————————————————————";
        cout << "\nEnter your choice ";
        cin >> ch;
        switch (ch)
        {
        case 1:
            cout << "Enter the x1 coordinate ";
            cin >> x1;
            cout << "Enter the y1 coordinate ";
            cin >> y1;
            cout << "Enter the x2 coordinate ";
            cin >> x2;
            cout << "Enter the y2 coordinate ";
            cin >> y2;
            initgraph(&gd, &gm, NULL);
            p.SRtri(x1, y1, x1, y2);
            p.SRtri(x1, y1, x2, y1);
            p.SRtri(x1, y2, x2, y2);
            p.SRtri(x2, y1, x2, y2);
            delay(3000);
            closegraph();
            break;
        case 2:
            cout << "Enter the x1 coordinate ";
            cin >> x1;
            cout << "Enter the y1 coordinate ";
            cin >> y1;
            cout << "Enter the x2 coordinate ";
            cin >> x2;
            cout << "Enter the y2 coordinate ";
            cin >> y2;
            initgraph(&gd, &gm, NULL);
            p.SRtri(x1, y1, x1, y2);
            p.SRtri(x1, y1, x2, y1);
            p.SRtri(x1, y2, x2, y2);
            p.SRtri(x2, y1, x2, y2);
            delay(3000);
            closegraph();
            break;
        case 3:
            cout << "Enter the x1 coordinate ";
            cin >> x1;
            cout << "Enter the y1 coordinate ";
            cin >> y1;
            cout << "Enter the x2 coordinate ";
            cin >> x2;
            cout << "Enter the y2 coordinate ";
            cin >> y2;
            cout << "Enter the x3 coordinate ";
            cin >> x3;
            cout << "Enter the y3 coordinate ";
            cin >> y3;
            initgraph(&gd, &gm, NULL);
            p.SRtri(x1, y1, x2, y2);
            p.SRtri(x2, y2, x3, y3);
            p.SRtri(x3, y3, x1, y1);
            delay(3000);
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
