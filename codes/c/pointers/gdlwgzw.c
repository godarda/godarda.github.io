// ----------------------------------------------------------------------------------------------------
// Title          : C program to print the length of a given array without using sizeof
// File Name      : gdlwgzw.c
// Compiled       : gcc (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <stdio.h>
int main()
{
    int min, max;
    int arr[5] = {100, 15, 8, 45, 93};
    int length = *(&arr + 1) - arr;
    printf("Length of a given array is %d", length);
    return 0;
}
