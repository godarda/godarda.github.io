// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to print the square of the numbers
// File Name      : gdvqyfg.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
    int i, j, n;
    cout<<"How many numbers you want to print ";
    cin>>n;
    cout<<"—————————————————————————————";
    cout<<"\nNumbers |"<<" Squares\n";
    cout<<"—————————————————————————————\n";
    for (int i = 1; i <= n; i++)
    {
        j = i * i;
        cout<<setw(3)<<i<<"     | "<<"  "<<j<<"\n";
    }
    cout<<"—————————————————————————————\n";
    return 0;
}
