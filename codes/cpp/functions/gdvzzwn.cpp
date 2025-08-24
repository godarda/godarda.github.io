// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to print the current date and time
// File Name      : gdvzzwn.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <iostream>
#include <iomanip>
#include <ctime>
using namespace std;
int main()
{
    int tm_sec, tm_min, tm_hour, tm_mday, tm_mon, tm_wday, tm_yday, counter = 0;
    time_t t;
    time(&t);
    tm *ltm = localtime(&t);
    cout<<"———————————————————————————————————————————";
    cout<<"\nProgram to print the current date & time\n";
    cout<<"———————————————————————————————————————————\n";
    cout<<"Date "<<setw(11)<<"| "<<(ltm->tm_mday)<<"/"<<(ltm->tm_mon) + 1<<"/"<<(ltm->tm_year) + 1900<<"\n";
    cout<<"Hours "<<setw(10)<<"| "<<ltm->tm_hour<<"\n";
    cout<<"Minutes "<<setw(8)<<"| "<<ltm->tm_min<<"\n";
    cout<<"Seconds "<<setw(8)<<"| "<<ltm->tm_sec<<"\n";
    cout<<"Year "<<setw(11)<<"| "<<1900 + ltm->tm_year<<"\n";
    cout<<"Current Time "<<setw(3)<<"| "<<ltm->tm_hour<<":"<<ltm->tm_min<<":"<<ltm->tm_sec<<"\n";
    cout<<"Date Of Month "<<setw(1)<<"| "<<ltm->tm_mday<<"\n";
    cout<<"Current Month "<<setw(1)<<"| "<<1 + ltm->tm_mon<<"\n";
    cout<<"Day Of Week "<<setw(4)<<"| "<<ltm->tm_wday<<"\n";
    cout<<"Days In Year "<<setw(3)<<"| "<<ltm->tm_yday<<"\n";
    cout<<"\n"<<ctime(&t);
    cout<<"———————————————————————————————————————————\n";
    return 0;
}
