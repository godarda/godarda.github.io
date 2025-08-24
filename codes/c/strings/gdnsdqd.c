// ----------------------------------------------------------------------------------------------------
// Title          : C program to reverse a given string
// File Name      : gdnsdqd.c
// Compiled       : gcc (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <stdio.h>
#include <string.h>
int main()
{
    char s[50], temp;
    printf("———————————————————————————————————————————");
    printf("\nProgram to reverse a given string");
    printf("\n———————————————————————————————————————————");
    printf("\nEnter the string ");
    scanf("%s", s);
    for (int i = 0, j = strlen(s) - 1; i < j; i++, j--)
    {
        temp = s[i];
        s[i] = s[j];
        s[j] = temp;
    }
    printf("\nThe reverse string is %s", s);
    printf("\n———————————————————————————————————————————\n");
    return 0;
}
