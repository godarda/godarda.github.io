// ----------------------------------------------------------------------------------------------------
// Title          : C program to find the address of variables
// File Name      : gdvdpgg.c
// Compiled       : gcc (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <stdio.h>
#include <string.h>
int main()
{
    int a = 10;
    char *string = "Hello World";
    char s = 'H';
    double d = 23.98908;
    long l = 343247891370492;
    // register b=10;
    // can't find the address of register variables
    printf("———————————————————————————————————————————");
    printf("\nProgram to find address of variables ");
    printf("\n———————————————————————————————————————————");
    printf("\nAddress of a      | %p", &a);
    printf("\nAddress of string | %p", &string);
    printf("\nAddress of s      | %p", &s);
    printf("\nAddress of d      | %p", &d);
    printf("\nAddress of l      | %p", &l);
    printf("\nmain address      | %p", main);
    printf("\nmain address      | %p", (void *)&main);
    printf("\n———————————————————————————————————————————\n");
    return 0;
}
