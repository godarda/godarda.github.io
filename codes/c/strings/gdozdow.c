// ----------------------------------------------------------------------------------------------------
// Title          : C program to concatenate the given strings
// File Name      : gdozdow.c
// Compiled       : gcc (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <stdio.h>
#include <string.h>
int main()
{
    char a[20], b[20];
    printf("———————————————————————————————————————————");
    printf("\nProgram to concatenate the two strings");
    printf("\n———————————————————————————————————————————");
    printf("\nEnter the 1st string ");
    scanf("%s", a);
    printf("\nEnter the 2nd string ");
    scanf("%s", b);
    strcat(a, b);
    printf("\nThe concatenated string is %s", a);
    printf("\n———————————————————————————————————————————\n");
    return 0;
}
