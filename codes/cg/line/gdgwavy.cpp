// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to draw a Pixel by accepting coordinates from the user
// File Name      : gdgwavy.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <graphics.h>
#include <iostream>
using namespace std;
int main()
{
    int gd = 0, gm = 9, x1, y1;
    cout << "Enter the x coordinate ";
    cin >> x1;
    cout << "Enter the y coordinate ";
    cin >> y1;
    initgraph(&gd, &gm, NULL);
    putpixel(x1, y1, 15);
    delay(2000);
    return 0;
}
