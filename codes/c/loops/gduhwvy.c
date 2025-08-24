// ----------------------------------------------------------------------------------------------------
// Title          : C program to reverse a given number
// File Name      : gduhwvy.c
// Compiled       : gcc (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <stdio.h>
int main()
{
    int n, temp;
    printf("———————————————————————————————————————————");
    printf("\nProgram to reverse a given number");
    printf("\n———————————————————————————————————————————");
    printf("\nEnter the number ");
    scanf("%d", &n);
    if (n < 10)
    {
        printf("\nUnable to reverse the negative and single-digit number.");
    }
    else
    {
        printf("\nThe reverse number is ");
        while (n / 10 != 0)
        {
            temp = n % 10;
            n = n / 10;
            printf("%d", temp);
        }
        printf("%d", n);
    }
    printf("\n———————————————————————————————————————————\n");
    return 0;
}
