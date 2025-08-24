// ----------------------------------------------------------------------------------------------------
// Title          : C++ program for addition of numbers using a function
// File Name      : gdtaync.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <iostream>
using namespace std;
int add(int a = 7, int b = 8)
{
    return a + b;
}
int main()
{
    cout<<add()<<"\n";
    return 0;
}
