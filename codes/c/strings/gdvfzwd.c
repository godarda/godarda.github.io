// ----------------------------------------------------------------------------------------------------
// Title          : C program to convert lowercase to an uppercase string
// File Name      : gdvfzwd.c
// Compiled       : gcc (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <stdio.h>
#include <string.h>
int main()
{
    char s[20];
    int i;
    printf("———————————————————————————————————————————");
    printf("\nProgram to convert lower to an uppercase string");
    printf("\n———————————————————————————————————————————");
    printf("\nEnter the string ");
    scanf("%s", s);
    for (i = 0; i <= strlen(s); i++)
    {
        if (s[i] >= 97 && s[i] <= 122)
            s[i] = s[i] - 32;
    }
    printf("\nThe uppercase string is %s", s);
    printf("\n———————————————————————————————————————————\n");
    return 0;
}
