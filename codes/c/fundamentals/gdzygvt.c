// ----------------------------------------------------------------------------------------------------
// Title          : C program to perform the arithmetic operations by accepting the inputs
// File Name      : gdzygvt.c
// Compiled       : gcc (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <stdio.h>
int main()
{
    float a, b, c;
    printf("———————————————————————————————————————————");
    printf("\nProgram to perform arithmetic operations");
    printf("\n———————————————————————————————————————————");
    printf("\nEnter the 1st number ");
    scanf("%f", &a);
    printf("\nEnter the 2nd number ");
    scanf("%f", &b);
    printf("———————————————————————————");
    c = a + b;
    printf("\n      Addition | %f", c);
    c = a - b;
    printf("\n   Subtraction | %f", c);
    c = a * b;
    printf("\nMultiplication | %f", c);
    c = a / b;
    printf("\n      Division | %f", c);
    printf("\n———————————————————————————\n");
    c = (a + b) / 2;
    printf("\nAverage of two numbers is %f", c);
    printf("\n———————————————————————————————————————————\n");
    return 0;
}
