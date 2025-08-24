// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to check whether a given string is a palindrome
// File Name      : gdyxqgg.cpp
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
    cout<<"\nProgram to check string is palindrome | not";
    cout<<"\n———————————————————————————————————————————";
    string s1, s2;
    cout<<"\nEnter the string ";
    getline(cin, s1);
    s2 = s1;
    reverse(s1.begin(), s1.end());
    if (s1 == s2)
    {
        cout<<"\n"
            <<s2<<" is a palindrome";
    }
    else
    {
        cout<<"\n"
            <<s2<<" is not a palindrome";
    }
    cout<<"\n———————————————————————————————————————————\n";
}
