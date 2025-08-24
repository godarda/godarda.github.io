// ----------------------------------------------------------------------------------------------------
// Title          : C program to print the star diamond pattern
// File Name      : gddysru.c
// Compiled       : gcc (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <stdio.h>
int main()
{
    int i, j;
    for (i = 1; i <= 7; i++)
    {
        for (j = 1; j <= 7 - i; j++)
        {
            printf(" ");
        }
        for (j = 1; j <= i; j++)
        {
            printf("* ");
        }
        printf("\n");
    }
    for (i = 6; i >= 1; i--)
    {
        for (j = 1; j <= 6 - i; j++)
        {
            printf(" ");
        }
        for (j = 1; j <= i; j++)
        {
            printf(" *");
        }
        printf("\n");
    }
}
