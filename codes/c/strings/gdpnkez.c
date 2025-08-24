// ----------------------------------------------------------------------------------------------------
// Title          : C program to find the length of a given string
// File Name      : gdpnkez.c
// Compiled       : gcc (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <stdio.h>
#include <string.h>
int main()
{
    char s[50];
    printf("———————————————————————————————————————————");
    printf("\nProgram to print length of a given string");
    printf("\n———————————————————————————————————————————");
    printf("\nEnter the string ");
    scanf("%s", s);
    int l = strlen(s);
    printf("\nLength of string is %d", l);
    printf("\n———————————————————————————————————————————\n");
    return 0;
}
