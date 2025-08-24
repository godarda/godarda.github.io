// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to demonstrate the use of goto statement
// File Name      : gdinkrg.cpp
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
    if (n % 2 == 0)
    {
        goto EVEN;
    }
    else
    {
        goto ODD;
    }
EVEN:
    cout<<n<<" is an EVEN number \n";
    return (0);
ODD:
    cout<<n<<" is an ODD number \n";
    return 0;
}
