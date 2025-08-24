// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to find the factorial of a given number
// File Name      : gdvzgge.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <iostream>
using namespace std;
int main()
{
    long i, n, fact = 1;
    cout<<"———————————————————————————————————————————";
    cout<<"\nProgram to find the factorial of a given number ";
    cout<<"\n———————————————————————————————————————————";
    cout<<"\nEnter the number ";
    cin>>n;
    if (n > 20 || n < 0)
    {
        cout<<"\nOOP's can't find "<<n<<"!";
    }
    else
    {
        for (i = 1; i <= n; i++)
        {
            fact = fact * i;
        }
        cout<<"\nFactorial of "<<n<<" = "<<fact;
    }
    cout<<"\n———————————————————————————————————————————\n";
    return 0;
}
