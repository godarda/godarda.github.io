// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to check the given number is positive or negative
// File Name      : gdgwhse.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <iostream>
using namespace std;
int main()
{
    int n;
    cout<<"Enter a number ";
    cin>>n;
    if (n < 0)
    {
        cout<<"Entered number is negative"<<endl;
    }
    else if (n > 0)
    {
        cout<<"Entered number is positive"<<endl;
    }
    else
    {
        cout<<"Entered number is zero"<<endl;
    }
    return 0;
}
