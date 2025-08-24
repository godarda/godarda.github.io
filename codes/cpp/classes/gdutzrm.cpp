// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to demonstrate the use of class and object
// File Name      : gdutzrm.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <iostream>
using namespace std;
class gd
{
public:
    void add()
    {
        cout<<"The addition of 10+10="<<10 + 10<<"\n";
    }
};
int main()
{
    gd g;
    g.add();
    return 0;
}
