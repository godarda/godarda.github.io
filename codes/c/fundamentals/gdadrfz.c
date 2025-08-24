// ----------------------------------------------------------------------------------------------------
// Title          : C program to perform the arithmetic operations
// File Name      : gdadrfz.c
// Compiled       : gcc (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <stdio.h>
int main()
{
    int a = 0, b = 1;
    printf("———————————————————————————————————————————");
    printf("\nProgram to perform arithmetic operations");
    printf("\n———————————————————————————————————————————");
    printf("\nValue of a   | %d ", a);
    printf("\nValue of b   | %d ", b);
    printf("\nValue of %d/%d | %d ", a, b, (a / b));
    printf("\nValue of %d+%d | %d ", a, b, (a + b));
    printf("\nValue of %d-%d | %d ", a, b, (a - b));
    printf("\nValue of %d*%d | %d ", a, b, (a * b));
    printf("\nValue of a++ | %d ", a++);
    printf("\nValue of ++a | %d ", ++a);
    printf("\n———————————————————————————————————————————\n");
    return 0;
}
