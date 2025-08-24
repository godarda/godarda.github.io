// ----------------------------------------------------------------------------------------------------
// Title          : C++ implementation of the stack and its operations
// File Name      : gduqyab.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include<iostream>
using namespace std;
int stack[100];
int top=-1; 
int main()
{
    int n,e;
    cout<<"———————————————————————————————————————————";
    cout<<"\nImplementation of a stack\n";
    cout<<"———————————————————————————————————————————";
    cout<<"\nNumbers of elements in a Stack ";
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>e;
        stack[++top] = e;
    }
    if(top<0) 
    {
        cout<<"\nStack is empty";
    } 
    cout<<"\nStack view\n";
    for(int i=top;i>=0;i--)
    {
        cout<<"| "<<stack[i]<<" |"<<endl;
    } 
    cout<<"———————————————————————————————————————————\n";
    return 0;
}
