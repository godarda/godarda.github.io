// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to print the given matrix
// File Name      : gdaziwv.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <iostream>
using namespace std;
int main()
{
    int a[10][10], i, j, m, n;
    cout<<"Enter the number of row(s) ";
    cin>>m;
    cout<<"Enter the number of column(s) ";
    cin>>n;
    if (m * n <= 0 || m && n < 0)
    {
        cout<<"-------------------------------------------";
        cout<<"\nEnter the valid number of rows and columns";
        cout<<"\n-------------------------------------------\n";
    }
    else
    {
        cout<<"\nEnter elements for matrix A \n";
        for (i = 1; i <= m; i++)
        {
            for (j = 1; j <= n; j++)
            {
                cout<<"["<<i<<"]"
                    <<"["<<j<<"]=";
                cin>>a[i][j];
            }
            cout<<"\n";
        }
        cout<<"Matrix A is \n";
        for (i = 1; i <= m; i++)
        {
            for (j = 1; j <= n; j++)
            {
                cout<<"\t"<<a[i][j];
            }
            cout<<"\n";
        }
    }
    return 0;
}
