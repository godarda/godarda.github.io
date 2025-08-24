// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to draw a line by accepting coordinates from the user
// File Name      : gddzqyg.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <graphics.h>
#include <iostream>
using namespace std;
int main()
{
    int gd = 0, gm = 9, x1, y1, x2, y2;
    cout << "Enter the x1 coordinate ";
    cin >> x1;
    cout << "Enter the y1 coordinate ";
    cin >> y1;
    cout << "Enter the x2 coordinate ";
    cin >> x2;
    cout << "Enter the y2 coordinate ";
    cin >> y2;
    initgraph(&gd, &gm, NULL);
    line(x1, y1, x2, y2);
    delay(2000);
    return 0;
}
