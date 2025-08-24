// ----------------------------------------------------------------------------------------------------
// Title          : C program to convert a binary number to an equivalent decimal number
// File Name      : gdmwzzz.c
// Compiled       : gcc (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <stdio.h>
int main()
{
    long n;
    int r, dn = 0, i = 1;
    printf("———————————————————————————————————————————");
    printf("\nProgram to convert a binary number to decimal");
    printf("\n———————————————————————————————————————————");
    printf("\nEnter the binary number ");
    scanf("%ld", &n);
    while (n != 0)
    {
        r = n % 10;
        dn = dn + r * i;
        i = i * 2;
        n = n / 10;
    }
    printf("\nEquivalent decimal number is %d", dn);
    printf("\n———————————————————————————————————————————\n");
    return 0;
}
