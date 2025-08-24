// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to print the floating-point numbers
// File Name      : gdwangz.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <iostream>
using namespace std;
int main()
{
    float i = 1;
    do
    {
        cout<<i<<"\n";
        i = i + 0.1;
    } while (i <= 2.1);
    return 0;
}
