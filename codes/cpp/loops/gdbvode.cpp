// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to print the star pyramid patterns
// File Name      : gdbvode.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <iostream>
using namespace std;
int main()
{
    int i, j;
    for (i = 1; i <= 10; i++)
    {
        for (j = 1; j <= i; j++)
        {
            cout<<"*";
        }
        cout<<"\n";
    }
    return 0;
}
