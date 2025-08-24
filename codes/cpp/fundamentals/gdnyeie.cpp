// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to calculate the area and circumference of a circle
// File Name      : gdnyeie.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <iostream>
using namespace std;
#define PI 3.141592654
int main()
{
    float R;
    cout<<"———————————————————————————————————————————";
    cout<<"\nProgram to calculate the area and circumference of a circle";
    cout<<"\n———————————————————————————————————————————";
    cout<<"\nEnter the radius of a circle ";
    cin>>R;
    cout<<"\nThe area of a circle is "<<PI * R * R;
    cout<<"\nThe circumference of a circle is "<<2 * PI * R;
    cout<<"\n———————————————————————————————————————————\n";
    return 0;
}
