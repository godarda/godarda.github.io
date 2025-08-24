// ----------------------------------------------------------------------------------------------------
// Title          : C program to check the given number is even or odd
// File Name      : gdcheqs.c
// Compiled       : gcc (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <stdio.h>
int main()
{
    int n, a;
    printf("———————————————————————————————————————————");
    printf("\nProgram for even-odd test of a given number");
    printf("\n———————————————————————————————————————————");
    printf("\nEnter a number ");
    scanf("%d", &n);
    if (n % 2 == 0)
    {
        printf("\n%d is EVEN number", n);
    }
    else
    {
        printf("\n%d is ODD number", n);
    }
    printf("\n———————————————————————————————————————————\n");
    return 0;
}
