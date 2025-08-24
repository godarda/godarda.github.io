// ----------------------------------------------------------------------------------------------------
// Title          : C program to print alphabets using the ASCII values
// File Name      : gdcdepo.c
// Compiled       : gcc (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <stdio.h>
int main()
{
    int i;
    for (i = 65; i < 91; i++)
    {
        printf("%c ", i);
    }
    printf("\n");
    return 0;
}
