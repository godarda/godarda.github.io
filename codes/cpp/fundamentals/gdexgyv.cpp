// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to perform the assignment operations
// File Name      : gdexgyv.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <iostream>
using namespace std;
int main()
{
    int a = 0, b = 1;
    cout<<"———————————————————————————————————————————";
    cout<<"\nProgram to perform the assignment operations ";
    cout<<"\n———————————————————————————————————————————";
    cout<<"\nValue of a      | "<<a;
    cout<<"\nValue of b      | "<<b;
    cout<<"\nValue of "<<a<<" += "<<b<<" | "<<(a += b);
    cout<<"\nValue of "<<a<<" -= "<<b<<" | "<<(a -= b);
    cout<<"\nValue of "<<a<<" *= "<<b<<" | "<<(a *= b);
    cout<<"\nValue of "<<a<<" /= "<<b<<" | "<<(a /= b);
    cout<<"\nValue of "<<a<<" %= "<<b<<" | "<<(a %= b);
    cout<<"\nValue of "<<a<<" ^= "<<b<<" | "<<(a ^= b);
    cout<<"\nValue of "<<a<<" |= "<<b<<" | "<<(a |= b);
    cout<<"\nValue of "<<a<<" &= "<<b<<" | "<<(a &= b);
    cout<<"\n———————————————————————————————————————————\n";
    return 0;
}
