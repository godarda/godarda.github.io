// ----------------------------------------------------------------------------------------------------
// Title          : C program to print the alphabets diamond pattern
// File Name      : gdzsayg.c
// Compiled       : gcc (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <stdio.h>
int main()
{
    int a = 65, n = 12, i, j, k;
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < (n - i); j++)
            printf(" ");
        for (k = 0; k <= i * 2; k++)
            printf("%c", a + k);
        printf("\n");
    }
    for (i = n; i >= 0; i--)
    {
        for (j = 0; j < n - i; j++)
            printf(" ");
        for (k = 0; k <= i * 2; k++)
            printf("%c", a + k);
        printf("\n");
    }
    return 0;
}
