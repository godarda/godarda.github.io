// ----------------------------------------------------------------------------------------------------
// Title          : C program to copy the given string
// File Name      : gdtwwpw.c
// Compiled       : gcc (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <stdio.h>
#include <string.h>
int main()
{
    char s1[20] = "Hello, World!";
    char s2[20];
    printf("———————————————————————————————————————————");
    printf("\nProgram to copy the given string");
    printf("\n———————————————————————————————————————————");
    printf("\nInput string %s ", s1);
    strcpy(s2, s1);

    printf("\n\nThe copied string is %s ", s2);
    printf("\n———————————————————————————————————————————\n");
    return 0;
}
