// ----------------------------------------------------------------------------------------------------
// Title          : C++ implementation of Prim's spanning tree algorithm
// File Name      : gdbuzge.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include<iostream>
using namespace std;
int weight[10][10],nodes;
int visited[10];

class prims
{
    int i,j,min,k,l,m,total_cost;
    public:
    void getdata();
    void matrix();
    void MST();
};

void prims::getdata()
{
    for(i=0;i<nodes;i++)
    {
        visited[i]=0;
    }
    cout<<"———————————————————————————————————————————\n";
    cout<<"Program for the Prim's algorithm\n";
    cout<<"———————————————————————————————————————————\n";
    cout<<"Enter the total number of nodes ";
    cin>>nodes;
    cout<<"\nEnter the distance of edges\n";
    for(i=0;i<nodes;i++)
    {
        for(j=0;j<nodes;j++)
        {
            cin>>weight[i][j];
        }
        cout<<"\n";
    }
}

void prims::matrix()
{
    cout<<"Adjacency matrix is\n ";
    for(i=0;i<nodes;i++)
    {
        for(j=0;j<nodes;j++)
        {
            cout<<"\t"<<weight[i][j];
        }
        cout<<"\n";
    }
}

void prims::MST()
{
    min=9999;
    total_cost=0;
    for(i=0;i<nodes;i++)
    {
        for(j=0;j<nodes;j++)
        {
            if(weight[i][j]<min&&weight[i][j]!=0)
            {
                min=weight[i][j];
                k=i;
                l=j;
            }
        }
    }
    cout<<"\nEdge "<<k<<"-"<<l<<" Having Distance "<<min;
    visited[k]=1;
    visited[l]=1;
    total_cost=min;
    for(m=0;m<nodes-2;m++)
    {
        min=9999;
        for(i=0;i<nodes;i++)
        {
            if(visited[i]==1)
            {
                for(j=0;j<nodes;j++)
                {
                    if(visited[j]!=1)
                    {
                        if(weight[i][j]<min&&weight[i][j]!=0)
                        {
                        min=weight[i][j];
                        k=i;
                        l=j;
                        }
                    }
                }
            }
        }
        cout<<"\nEdge "<<k<<"-"<<l<<" having distance "<<min;
        visited[k]=1;
        visited[l]=1;
        total_cost=total_cost+min;
    }
    cout<<"\nTotal cost is "<<total_cost;
    cout<<"\n";
}
int main()
{
    prims p;
    p.getdata();
    p.matrix();
    p.MST();
    return 0;
}
