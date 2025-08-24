// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to add the members of two different classes using the friend function
// File Name      : gdmeaby.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <iostream>
using namespace std;
class WhiteBank;
class BlackBank
{
private:
    int total_money_bb;

public:
    BlackBank() : total_money_bb(200) {}
    friend int total_amount(WhiteBank, BlackBank);
};

class WhiteBank
{
private:
    int total_money_wb;

public:
    WhiteBank() : total_money_wb(200) {}
    friend int total_amount(WhiteBank, BlackBank);
};

int total_amount(WhiteBank wb, BlackBank bb)
{
    return (wb.total_money_wb + bb.total_money_bb);
}

int main()
{
    WhiteBank wb;
    BlackBank bb;
    cout<<"Total Bank Amount "<<total_amount(wb, bb)<<endl;
    return 0;
}
