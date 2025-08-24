// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to perform arithmetic operations by accepting inputs from a user
// File Name      : gdzzhqg.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <iostream>
using namespace std;
int main()
{
    float a, b;
    cout<<"———————————————————————————————————————————";
    cout<<"\nProgram to perform the arithmetic operations";
    cout<<"\n———————————————————————————————————————————";
    cout<<"\nEnter the 1st number ";
    cin>>a;
    cout<<"\nEnter the 2nd number ";
    cin>>b;
    cout<<"——————————————————————————";
    cout<<"\nAddition       | "<<a<<"+"<<b<<"="<<a + b;
    cout<<"\nSubtraction    | "<<a<<"-"<<b<<"="<<a - b;
    cout<<"\nMultiplication | "<<a<<"*"<<b<<"="<<a * b;
    cout<<"\nDivision       | "<<a<<"/"<<b<<"="<<a / b;
    cout<<"\n——————————————————————————";
    cout<<"\nAverage of 2 numbers is "<<(a + b) / 2;
    cout<<"\n———————————————————————————————————————————\n";
    return 0;
}
