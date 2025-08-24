// ----------------------------------------------------------------------------------------------------
// Title          : C program to print the sum of all numbers in a given array
// File Name      : gdavnal.c
// Compiled       : gcc (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <stdio.h>
int main()
{
    int sum = 0;
    int arr[5] = {100, 15, 8, 45, 93};
    for (int i = 0; i < 5; i++)
    {
        sum = sum + arr[i];
    }
    printf("The addition of a given array is %d ", sum);
    return 0;
}
