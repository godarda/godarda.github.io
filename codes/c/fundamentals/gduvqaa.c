// ----------------------------------------------------------------------------------------------------
// Title          : C Hello World program
// File Name      : gduvqaa.c
// Compiled       : gcc (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <stdio.h>
int main()
{
    printf("Hello, World!\n");

    char *str = "Hello, World!\n";
    printf("%s", str);

    puts("Hello, World!\n");

    printf("%c%c%c%c%c%c%c%c%c%c%c\n", 72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100);
    return 0;
}
