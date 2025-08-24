// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to demonstrate the use of break and continue statements
// File Name      : gdidhad.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <iostream>
using namespace std;
int main()
{
    for (int i = 0; i < 10; i++)
    {
        if (i == 5)
        {
            break;
        }
        cout<<i<<endl;
    }
    return 0;
}
