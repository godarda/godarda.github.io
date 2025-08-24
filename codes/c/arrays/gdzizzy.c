// ----------------------------------------------------------------------------------------------------
// Title          : C program to print the given array
// File Name      : gdzizzy.c
// Compiled       : gcc (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <stdio.h>
int main()
{
    int arr[5] = {1, 2, 3, 4, 5};
    for (int i = 0; i < 5; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}
