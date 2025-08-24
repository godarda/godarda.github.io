// ----------------------------------------------------------------------------------------------------
// Title          : C++ program to perform the string operations
// File Name      : gdpzcle.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <iostream>
#include <cstring>
using namespace std;
int main()
{
    char s1[] = "Hello";
    string s2("\"Hello\"");
    string s3("\'World\'");

    cout<<"———————————————————————————————————————————";
    cout<<"\nProgram for the string operations";
    cout<<"\n———————————————————————————————————————————";
    cout<<"\nString s1 | "<<s1;
    cout<<"\nString s2 | "<<s2;
    cout<<"\nString s3 | "<<s3;
    cout<<"\n———————————————————————————————————————————";

    cout<<"\nSize of string s2     | "<<s2.size();
    cout<<"\nLength of string s1   | "<<strlen(s1);
    cout<<"\nLength of string s3   | "<<s3.length();
    cout<<"\nCapacity of string s2 | "<<s2.capacity();
    cout<<"\nConcatination s1+s3   | "<<s1 + s3;
    cout<<"\nMax size of string s2 | "<<s2.max_size();
    cout<<"\n———————————————————————————————————————————";
    s2.swap(s3);
    cout<<"\nAfter swapping the strings...";
    cout<<"\n———————————————————————————————————————————";
    cout<<"\ns3 | "<<s3;
    cout<<"\ns2 | "<<s2;
    cout<<"\n———————————————————————————————————————————";

    cout<<"\nInsert s3 into s2     | "<<s2.insert(3, s3);
    s2.erase(3, 7);
    cout<<"\nDelete inserted string| "<<s2;
    s2.replace(0, 0, s3);
    cout<<"\nReplace string AsItIs | "<<s2;
    s2.append(s3);
    cout<<"\nAppend s2 To s3       | "<<s2;
    s2.assign(s3);
    cout<<"\ns3 Assign string s2   | "<<s2;
    cout<<"\n———————————————————————————————————————————\n";
    return 0;
}
