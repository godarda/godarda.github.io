// ----------------------------------------------------------------------------------------------------
// Title          : C program to find the factorial of a given number using recursion
// File Name      : gdhfycr.c
// Compiled       : gcc (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <stdio.h>
long facto(long x);
int main()
{
    long n, a;
    printf("———————————————————————————————————————————");
    printf("\nProgram to find the factorial of a given number");
    printf("\n———————————————————————————————————————————");
    printf("\nEnter the number ");
    scanf("%ld", &n);
    if (n < 0)
    {
        printf("Please enter a positive number or zero");
    }
    else if (n >= 26)
    {
        printf("Please enter a number less than 26");
    }
    else
    {
        a = facto(n);
        printf("\nThe factorial of %ld is %ld", n, a);
    }
    printf("\n———————————————————————————————————————————\n");
    return 0;
}
long facto(long n)
{
    if (n >= 1)
    {
        return n * facto(n - 1);
    }
    else
    {
        return 1;
    }
}
