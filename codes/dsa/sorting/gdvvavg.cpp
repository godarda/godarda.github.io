// ----------------------------------------------------------------------------------------------------
// Title          : C++ progarm for optimized Bubble Sort
// File Name      : gdvvavg.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include<iostream>
using namespace std;

void BubbleSort(int a[], int n)
{
    for(int i=0;i<(n-1);i++)
    {
        for(int j=0;j<n-i-1;j++)
        {
            if(a[j]>a[j+1])
            {
                a[j]=a[j]+a[j+1];
                a[j+1]=a[j]-a[j+1];
                a[j]=a[j]-a[j+1];
            }
        }
    }
}

int main()
{
    int n,i;
    cout<<"———————————————————————————————————————————";
    cout<<"\nImplementation of a Bubble Sort\n";
    cout<<"———————————————————————————————————————————";
    cout<<"\nEnter the number of elements ";
    cin>>n;
    int a[n];
    for(i=0;i<n;i++)
    {
        cin>>a[i];
    }
    
    BubbleSort(a,n);
    
    cout<<"\nSorted elements ";
    for(i=0;i<n;i++)
    {
        cout<<a[i]<<" ";
    }
    cout<<"\n———————————————————————————————————————————\n";
    return 0;
}
