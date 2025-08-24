// ----------------------------------------------------------------------------------------------------
// Title          : C menu-driven program for the arithmetic operations
// File Name      : gdvdeeg.c
// Compiled       : gcc (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>
int a, b, c;
void accept()
{
    printf("Enter the 1st number ");
    scanf("%d", &a);
    printf("Enter the 2nd number ");
    scanf("%d", &b);
}
int add(int a, int b)
{
    return a + b;
}
int sub(int a, int b)
{
    return a - b;
}
int mul(int a, int b)
{
    return a * b;
}
float division(float a, float b)
{
    return a / b;
}
int main()
{
    int ch;
    do
    {
        printf("\n———————————————————————————————————————————");
        printf("\nMenu-driven program for the arithmetic operations");
        printf("\n———————————————————————————————————————————");
        printf("\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit");
        printf("\n———————————————————————————————————————————");
        printf("\nEnter your choice ");
        scanf("%d", &ch);
        switch (ch)
        {
        case 1:
            accept();
            printf("Addition of %d+%d = %d", a, b, add(a, b));
            break;
        case 2:
            accept();
            printf("Subtraction of %d-%d = %d", a, b, sub(a, b));
            break;
        case 3:
            accept();
            printf("Multiplication of %d*%d = %d", a, b, mul(a, b));
            break;
        case 4:
            accept();
            printf("Division of %d/%d = %f", a, b, division(a, b));
            break;
        case 5:
            exit(0);
        default:
            printf("Wrong choice entered... Please try again\n");
        }
    } while (ch != 5);
    return 0;
}
