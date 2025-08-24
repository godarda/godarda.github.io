// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to reverse a given string using stack
// File Name      : gdywzwa.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <iostream>
#include <cstring>
#define SIZE 50
using namespace std;

int i, top = -1;
char stack[SIZE];

bool push(char element)
{
    if (top == (SIZE - 1))
    {
        cout<<"\nStack overflow";
        return false;
    }
    else
    {
        stack[++top] = element;
        return true;
    }
}

char pop()
{
    if (top == -1)
    {
        cout<<"\nStack underflow";
        return 0;
    }
    else
    {
        return stack[top--];
    }
}

int main()
{
    cout<<"———————————————————————————————————————————";
    cout<<"\nProgram to reverse a given string";
    cout<<"\n———————————————————————————————————————————";
    char s[50];
    cout<<"\nEnter the string ";
    cin>>s;
    for (i = 0; i < strlen(s); i++)
    {
        push(s[i]);
    }
    for (i = 0; i < strlen(s); i++)
    {
        s[i] = pop();
    }
    cout<<"\nThe reverse string is "<<s;
    cout<<"\n———————————————————————————————————————————\n";
    return 0;
}
