// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to print the addition of N numbers
// File Name      : gdwaaup.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <iostream>
using namespace std;
int main()
{
    int n, sum;
    cout<<"———————————————————————————————————————————";
    cout<<"\nProgram to print the addition of N numbers";
    cout<<"\n———————————————————————————————————————————";
    cout<<"\nEnter the number ";
    cin>>n;
    if (n >= 0)
    {
        sum = (n * (n + 1) / 2);
        cout<<"\nThe sum of first "<<n<<" natural numbers is = "<<sum;
    }
    else
    {
        cout<<"\nPlease enter +ve number ";
    }
    cout<<"\n———————————————————————————————————————————\n";
    return 0;
}
