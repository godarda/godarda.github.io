// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to swap the given strings
// File Name      : gdzdyvg.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <iostream>
#include <cstring>
using namespace std;
int main()
{
    string s1, s2, s3;
    cout<<"———————————————————————————————————————————";
    cout<<"\nProgram to swap the given strings";
    cout<<"\n———————————————————————————————————————————";
    cout<<"\ns1=";
    getline(cin, s1);
    cout<<"s2=";
    getline(cin, s2);
    s3 = s1;
    s1 = s2;
    s2 = s3;
    cout<<"———————————————————————————————————————————";
    cout<<"\nAfter swapping...";
    cout<<"\n———————————————————————————————————————————";
    cout<<"\ns1="<<s1;
    cout<<"\ns2="<<s2;
    cout<<"\n———————————————————————————————————————————\n";
    return 0;
}
