// ----------------------------------------------------------------------------------------------------
// Title          : C++ program for addition and subtraction of two matrices
// File Name      : gdauaoi.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <iostream>
using namespace std;
int main()
{
    int a[10][10], b[10][10], c[10][10], i, j, m, n;
    cout<<"———————————————————————————————————————————";
    cout<<"\nProgram for addition and subtraction of matrices\n";
    cout<<"———————————————————————————————————————————";
    cout<<"\nEnter the number of row(s) ";
    cin>>m;
    cout<<"Enter the number of column(s) ";
    cin>>n;
    if (m && n <= 0 || m * n <= 0)
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

        cout<<"Enter elements for matrix B \n";
        for (i = 1; i <= m; i++)
        {
            for (j = 1; j <= n; j++)
            {
                cout<<"["<<i<<"]"
                    <<"["<<j<<"]=";
                cin>>b[i][j];
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

        cout<<"Matrix B is \n";
        for (i = 1; i <= m; i++)
        {
            for (j = 1; j <= n; j++)
            {
                cout<<"\t"<<b[i][j];
            }
            cout<<"\n";
        }

        cout<<"The addition of matrix A and matrix B is\n";
        for (i = 1; i <= m; i++)
        {
            for (j = 1; j <= n; j++)
            {
                c[i][j] = a[i][j] + b[i][j];
                cout<<"\t"<<c[i][j];
            }
            cout<<"\n";
        }

        cout<<"The subtraction of matrix A and matrix B is\n";
        for (i = 1; i <= m; i++)
        {
            for (j = 1; j <= n; j++)
            {
                c[i][j] = a[i][j] - b[i][j];
                cout<<"\t"<<c[i][j];
            }
            cout<<"\n";
        }
    }
    cout<<"———————————————————————————————————————————\n";
    return 0;
}
