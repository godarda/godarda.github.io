// ----------------------------------------------------------------------------------------------------
// Title          : C program to check the equality of given numbers
// File Name      : gddwdgs.c
// Compiled       : gcc (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <stdio.h>
int main()
{
    float a, b;
    printf("———————————————————————————————————————————");
    printf("\nProgram to check the equality of given numbers");
    printf("\n———————————————————————————————————————————");
    printf("\nEnter the 1st number ");
    scanf("%f", &a);
    printf("\nEnter the 2nd number ");
    scanf("%f", &b);
    if (a < b)
    {
        printf("\n%f is less than %f", a, b);
    }
    else if (a == b)
    {
        printf("\n%f is equal to %f", a, b);
    }
    else
    {
        printf("\n%f is greater than %f", a, b);
    }
    printf("\n———————————————————————————————————————————\n");
    return 0;
}
