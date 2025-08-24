// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to demonstrate the use of constructors and destructors
// File Name      : gddvyma.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <iostream>
using namespace std;
class gd
{
public:
    gd()
    {
        cout<<"\nConstructor is called";
    }
    ~gd()
    {
        cout<<"\nDestructor is called";
    }
};
int main()
{
    gd g;
    gd();
    g.~gd();
}
