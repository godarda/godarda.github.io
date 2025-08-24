// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to check the equality of given numbers
// File Name      : gdkgzza.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <iostream>
using namespace std;
int main()
{
    int a, b;
    cout<<"———————————————————————————————————————————";
    cout<<"\nProgram to check the equality of given numbers\n";
    cout<<"———————————————————————————————————————————";
    cout<<"\nEnter the first number ";
    cin>>a;
    cout<<"Enter the second number ";
    cin>>b;
    if (a < b)
    {
        cout<<"\n"<<a<<" is less than "<<b;
    }
    else if (a == b)
    {
        cout<<"\n"<<a<<" is equal to "<<b;
    }
    else
    {
        cout<<"\n"<<a<<" is greater than "<<b;
    }
    cout<<"\n———————————————————————————————————————————\n";
    return 0;
}
