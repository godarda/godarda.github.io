// ----------------------------------------------------------------------------------------------------
// Title          : C++ implementation of Binary Search
// File Name      : gdecgzp.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include<iostream>
using namespace std;
void BinarySearch(int a[],int num,int first,int last)
{
    if(first>last)
    {
        cout<<"\nElement not found!"<<endl;
        cout<<"———————————————————————————————————————————\n";
    }
    else
    {
        int mid;
        mid=(first+last)/2;
        if(a[mid]==num)
        {
            cout<<"\nElement found at index "<<mid+1<<endl;
            cout<<"———————————————————————————————————————————\n";
        }
        else if(a[mid]>num)
        {
            BinarySearch(a,num,first,mid-1);
        }
        else
        {
            BinarySearch(a,num,mid+1,last);
        }
    }
}

int main()
{
    int n,i,j,num,end,beg,temp;
    cout<<"———————————————————————————————————————————";
    cout<<"\nImplementation of a Binary Search";
    cout<<"\n———————————————————————————————————————————";
    try
    {
        cout<<"\nHow many numbers you want to enter ";
        cin>>n;
        if(cin.fail()) throw "";
        int a[n];
        for(i=0;i<n;i++)
        {
            cout<<"Enter Number "<<i+1<<" | ";
            cin>>a[i];
        }
        for(i=0;i<n;i++)            
        {
            for(j=i+1;j<n;j++)
            {
                if(a[i]>a[j])
                {
                    temp=a[i];                     
                    a[i]=a[j];
                    a[j]=temp;
                }
            }
        }
        cout<<"\nSorted numbers ";
        for(i=0;i<n;i++)
        {
            cout<<a[i]<<" ";
        }
        beg=0;
        end=n-1;
        cout<<"\nEnter a number to be searched ";
        cin>>num;
        BinarySearch(a,num,beg,end);
    }
    catch(...)
    {
        cout<<"\nEnter the number please"<<endl;
        cout<<"———————————————————————————————————————————\n";
    }
    return(0);
}
