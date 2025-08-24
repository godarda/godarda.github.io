// ----------------------------------------------------------------------------------------------------
// Title          : C++ progarm for Bubble Sort
// File Name      : gdwzsgz.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include<iostream>
using namespace std;
int main()
{
    int n,a[50],i,j,temp;
    cout<<"———————————————————————————————————————————";
    cout<<"\nImplementation of a Bubble Sort\n";
    cout<<"———————————————————————————————————————————";
    cout<<"\nEnter the number of elements ";
    cin>>n;
    for(i=0;i<n;i++)
    {
        cin>>a[i];
    }

    for(i=0;i<(n-1);i++)
    {
        for(j=0;j<n-i-1;j++)
        {
            if(a[j]>a[j+1])
            {
                temp=a[j];
                a[j]=a[j+1];
                a[j+1]=temp;
            }
        }
    }

    cout<<"\nSorted elements ";
    for(i=0;i<n;i++)
    {
        cout<<a[i]<<" ";
    }
    cout<<"\n———————————————————————————————————————————\n";
    return 0;
}
