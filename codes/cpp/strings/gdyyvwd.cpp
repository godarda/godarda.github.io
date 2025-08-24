// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to reverse a given string using predefined methods
// File Name      : gdyyvwd.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main()
{
    cout<<"———————————————————————————————————————————";
    cout<<"\nProgram to reverse a given string";
    cout<<"\n———————————————————————————————————————————";
    string s;
    cout<<"\nEnter the string ";
    getline(cin, s);

    reverse(s.begin(), s.end());
    cout<<"\nThe reverse string is "<<s;
    cout<<"\n———————————————————————————————————————————\n";
}
