// ----------------------------------------------------------------------------------------------------
// Title          : C program to find the factorial of a given number
// File Name      : gdbudev.c
// Compiled       : gcc (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <stdio.h>
int facto(int);
int main()
{
    int n, a;
    printf("———————————————————————————————————————————");
    printf("\nProgram to find the factorial of a given number");
    printf("\n———————————————————————————————————————————");
    printf("\nEnter the number ");
    scanf("%d", &n);
    if (n < 0)
    {
        printf("Please enter a positive number or zero");
    }
    else if (n > 15)
    {
        printf("\nPlease enter a number less than 16");
    }
    else
    {
        a = facto(n);
        printf("\nThe factorial of %d is %d", n, a);
    }
    printf("\n———————————————————————————————————————————\n");
    return 0;
}
int facto(int n)
{
    int i, factorial = 1;
    for (i = 1; i <= n; i++)
    {
        factorial = factorial * i;
    }
    return (factorial);
}
