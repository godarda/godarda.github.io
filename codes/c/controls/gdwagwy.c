// ----------------------------------------------------------------------------------------------------
// Title          : C program to demonstrate the use of goto statement
// File Name      : gdwagwy.c
// Compiled       : gcc (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <stdio.h>
int main()
{
    int n, a;
    printf("Enter a number ");
    scanf("%d", &n);
    if (n % 2 == 0)
    {
        goto EVEN;
    }
    else
    {
        goto ODD;
    }
EVEN:
    printf("%d is an EVEN number\n", n);
    return (0);
ODD:
    printf("%d is an ODD number\n", n);
    return 0;
}
