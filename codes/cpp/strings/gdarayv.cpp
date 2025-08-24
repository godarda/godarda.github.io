// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to reverse a given string using recursion
// File Name      : gdarayv.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <iostream>
using namespace std;
void reverse(string &s, int l, int h)
{
    if (l < h)
    {
        swap(s[l], s[h]);
        reverse(s, l + 1, h - 1);
    }
}

int main()
{
    cout<<"———————————————————————————————————————————";
    cout<<"\nProgram to reverse a given string";
    cout<<"\n———————————————————————————————————————————";
    string s;
    cout<<"\nEnter the string ";
    cin>>s;
    reverse(s, 0, s.length() - 1);
    cout<<"\nThe reverse string is "<<s;
    cout<<"\n———————————————————————————————————————————\n";
}
