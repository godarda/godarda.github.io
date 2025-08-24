// ----------------------------------------------------------------------------------------------------
// Title          : C program to compare the given strings
// File Name      : gdgdpvh.c
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
    printf("\nProgram to compare two strings");
    printf("\n———————————————————————————————————————————");
    printf("\nEnter the 1st string ");
    scanf("%s", a);
    printf("\nEnter the 2nd string ");
    scanf("%s", b);
    int c = strcmp(a, b);
    if (c == 0)
    {
        printf("\nStrings are equal");
    }
    else
    {
        printf("\nStrings are unequal");
    }
    printf("\n———————————————————————————————————————————\n");
    return 0;
}
