// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to draw a sine wave
// File Name      : gdmtvba.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <iostream>
#include <graphics.h>
using namespace std;
int main()
{
    int gd = DETECT, gm;
    float x = 0, y, a;
LOOP:
    cout << "\nEnter the Amplitude value ";
    cin >> a;
    if (a >= 30 && a <= 200)
    {
        initgraph(&gd, &gm, NULL);
        line(0, 230, 620, 230);
        for (x = 0; x <= 600; x++)
        {
            y = 230 + (120 * sin(2 * 3.14 * x / 200));
            x = x + 3;
            putpixel(x, y, 14);
            outtextxy(x, y, (char*)"o");
            setcolor(2);
            line(x, y, x, 230);
            delay(50);
        }
        delay(3000);
    }
    else
    {
        cout << "\n------------------------------------------------";
        cout << "\nAmplitude must be in the range of [30-200]";
        cout << "\n------------------------------------------------";
        goto LOOP;
    }
    return 0;
}
