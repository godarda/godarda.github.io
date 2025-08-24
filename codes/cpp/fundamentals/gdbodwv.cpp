// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to find the size of data types
// File Name      : gdbodwv.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
    cout<<"———————————————————————————————————————————";
    cout<<"\nProgram to print the size of data types\n";
    cout<<"———————————————————————————————————————————";
    cout<<"\nThe size of int "<<setw(11)<<"| "<<sizeof(int)<<"\n";
    cout<<"The size of float "<<setw(9)<<"| "<<sizeof(float)<<"\n";
    cout<<"The size of short "<<setw(9)<<"| "<<sizeof(short)<<"\n";
    cout<<"The size of double "<<setw(8)<<"| "<<sizeof(double)<<"\n";
    cout<<"The size of long "<<setw(10)<<"| "<<sizeof(long)<<"\n";
    cout<<"The size of char "<<setw(10)<<"| "<<sizeof(char)<<"\n";
    cout<<"The size of bool "<<setw(10)<<"| "<<sizeof(bool)<<"\n";
    cout<<"The size of NULL "<<setw(10)<<"| "<<sizeof(NULL)<<"\n";
    cout<<"The size of wchar_t "<<setw(7)<<"| "<<sizeof(wchar_t)<<"\n";
    cout<<"Size of long int "<<setw(10)<<"| "<<sizeof(long int)<<"\n";
    cout<<"Size of short int "<<setw(9)<<"| "<<sizeof(short int)<<"\n";
    cout<<"Size of long double "<<setw(7)<<"| "<<sizeof(long double)<<"\n";
    cout<<"Size of signed int "<<setw(8)<<"| "<<sizeof(signed int)<<"\n";
    cout<<"Size of unsigned int "<<setw(6)<<"| "<<sizeof(unsigned int)<<"\n";
    cout<<"Size of signed char "<<setw(7)<<"| "<<sizeof(signed char)<<"\n";
    cout<<"Size of unsigned char "<<setw(5)<<"| "<<sizeof(unsigned char)<<"\n";
    cout<<"Size of long signed int "<<setw(3)<<"| "<<sizeof(long signed int)<<"\n";
    cout<<"Size of long unsigned int"<<setw(0)<<"| "<<sizeof(long unsigned int)<<"\n";
    cout<<"———————————————————————————————————————————\n";
    return 0;
}
