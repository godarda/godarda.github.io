// ----------------------------------------------------------------------------------------------------
// Title          : C++ program for call by value and call by reference
// File Name      : gdzddye.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <iostream>
using namespace std;
int add(int a, int b)
{
    a = 100;
    b = 100;
    int c = a + b;
    return c;
}
int main()
{
    int a = 20, b = 10, c;
    c = a + b;
    add(a, b);
    cout<<c<<endl;
}
