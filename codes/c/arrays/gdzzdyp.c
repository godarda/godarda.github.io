// ----------------------------------------------------------------------------------------------------
// Title          : C program to print the length of a given array
// File Name      : gdzzdyp.c
// Compiled       : gcc (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <stdio.h>
int main()
{
    int arr[] = {1, 2, 3, 4, 5};
    printf("Length of an array is %ld \n", (sizeof(arr) / sizeof(int)));
    return 0;
}
