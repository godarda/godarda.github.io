// ----------------------------------------------------------------------------------------------------
// Title          : C program to demonstrate the static and local variables
// File Name      : gddrnhk.c
// Compiled       : gcc (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <stdio.h>
int main()
{
    for (int i = 0; i < 5; i++)
    {
        static int a = 0;
        int b = 0;
        a++;
        b++;
        printf("Static:a = %d | Local:b = %d\n", a, b);
    }
    return 0;
}
