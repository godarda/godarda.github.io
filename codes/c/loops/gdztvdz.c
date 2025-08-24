// ----------------------------------------------------------------------------------------------------
// Title          : C program for the addition of N natural numbers
// File Name      : gdztvdz.c
// Compiled       : gcc (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <stdio.h>
int main()
{
    int n, sum;
    printf("———————————————————————————————————————————");
    printf("\nProgram for the addition of N numbers");
    printf("\n———————————————————————————————————————————");
    printf("\nEnter the number ");
    scanf("%d", &n);
    if (n > 0)
    {
        sum = (n * (n + 1) / 2);
        printf("\nSum of %d natural numbers = %d", n, sum);
    }
    else
    {
        printf("\nPlease enter the positive natural number");
    }
    printf("\n———————————————————————————————————————————\n");
    return 0;
}
