// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to print the ASCII values
// File Name      : gdvzpzf.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <iostream>
using namespace std;
int main()
{
    cout<<"———————————————————————————————————————————";
    cout<<"\nProgram to print the ASCII values";
    cout<<"\n———————————————————————————————————————————\n";
    for (int i = 32; i <= 126; i++)
    {
        cout<<i<<" -> "<<(char)i<<" ";
    }
    cout<<"\n———————————————————————————————————————————\n";
    return 0;
}
