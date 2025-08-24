// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to print the natural numbers
// File Name      : gdvydev.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <iostream>
using namespace std;
int main()
{
    int n, i;
    cout<<"How many numbers you want to print ";
    cin>>n;
    for (i = 1; i <= n; i++)
        cout<<i<<" ";
    cout<<"\n";
    return 0;
}
