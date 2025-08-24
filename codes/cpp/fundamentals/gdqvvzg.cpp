// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to find the range of data types
// File Name      : gdqvvzg.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <iostream>
#include <stdlib.h>
#include <climits>
#include <cmath>
#include <stdio.h>
#include <float.h>
using namespace std;
int main()
{
    cout<<"———————————————————————————————————————————";
    cout<<"\nProgram to print the range of data types";
    cout<<"\n———————————————————————————————————————————\n";
    cout<<"   Signed char  | "<<SCHAR_MIN<<" To "<<SCHAR_MAX<<"\n";
    cout<<" Unsigned char  |  0"<<" To "<<UCHAR_MAX<<"\n";
    cout<<"  Signed short  | "<<SHRT_MIN<<" To "<<SHRT_MAX<<"\n";
    cout<<" Unsigned short |  0"<<" To "<<USHRT_MAX<<"\n";
    cout<<"   Signed  int  | "<<INT_MIN<<" To "<<INT_MAX<<"\n";
    cout<<" Unsigned  int  |  0"<<" To "<<UINT_MAX<<"\n";
    cout<<"   Signed long  | "<<LONG_MIN<<" To "<<LONG_MAX<<"\n";
    cout<<" Unsigned long  |  0"<<" To "<<ULONG_MAX<<"\n";
    cout<<"         float  | "<<FLT_MIN<<" To "<<FLT_MAX<<"\n";
    cout<<"        double  | "<<DBL_MIN<<" To "<<DBL_MAX<<"\n";
    cout<<"———————————————————————————————————————————\n";

    cout<<"   Signed char  | "<<pow(-2, (1 * CHAR_BIT) - 1)<<" To "<<pow(+2, (1 * CHAR_BIT) - 1) - 1<<"\n";
    cout<<" Unsigned char  |  0"<<" To "<<pow(+2, (1 * CHAR_BIT)) - 1<<"\n";
    cout<<"  Signed short  | "<<pow(-2, (2 * CHAR_BIT) - 1)<<" To "<<pow(+2, (2 * CHAR_BIT) - 1) - 1<<"\n";
    cout<<"Unsigned short  |  0"<<" To "<<pow(+2, (2 * CHAR_BIT)) - 1<<"\n";
    cout<<"   Signed  int  | "<<pow(-2, (4 * CHAR_BIT) - 1)<<" To "<<pow(+2, (4 * CHAR_BIT) - 1) - 1<<"\n";
    cout<<" Unsigned  int  |  0"<<" To "<<pow(+2, (4 * CHAR_BIT)) - 1<<"\n";
    cout<<"   Signed long  | "<<pow(-2, (8 * CHAR_BIT) - 1)<<" To "<<pow(+2, (8 * CHAR_BIT) - 1) - 1<<"\n";
    cout<<" Unsigned long  |  0"<<" To "<<pow(+2, (8 * CHAR_BIT)) - 1<<"\n";
    cout<<"———————————————————————————————————————————\n";
    return (EXIT_SUCCESS);
}
