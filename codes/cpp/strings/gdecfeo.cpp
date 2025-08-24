// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to reverse a given string using loops
// File Name      : gdecfeo.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <iostream>
#include <cstring>
using namespace std;
int main()
{
    cout<<"———————————————————————————————————————————";
    cout<<"\nProgram to reverse a given string";
    cout<<"\n———————————————————————————————————————————";
    string s, r = "";
    cout<<"\nEnter the string ";
    getline(cin, s);
    for (int i = s.length() - 1; i >= 0; i--)
    {
        r = r + s[i];
    }
    cout<<"\nThe reverse string is "<<r;
    cout<<"\n———————————————————————————————————————————\n";
}
