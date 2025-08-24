// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to print the addition of numbers using constructor
// File Name      : gdtvfzm.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <iostream>
using namespace std;
class gd
{
    int a, b;

public:
    void add()
    {
        cout<<"The addition of "<<a<<"+"<<b<<"="<<(a + b)<<"\n";
    }
    gd()
    {
        a = 10;
        b = 10;
    }
};
int main()
{
    gd g;
    g.add();
    return 0;
}
