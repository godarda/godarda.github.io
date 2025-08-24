// ----------------------------------------------------------------------------------------------------
// Title          : C program to find the size of data types
// File Name      : gdmwpsv.c
// Compiled       : gcc (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <stdio.h>
int main()
{
    printf("———————————————————————————————————————————");
    printf("\nProgram to find the size of data types");
    printf("\n———————————————————————————————————————————");
    printf("\nvoid       | %ld byte", sizeof(void));
    printf("\nint        | %ld bytes", sizeof(int));
    printf("\nchar       | %ld bytes", sizeof(char));
    printf("\nfloat      | %ld bytes", sizeof(float));
    printf("\ndouble     | %ld bytes", sizeof(double));
    printf("\nlong       | %ld bytes", sizeof(long));
    printf("\nshort      | %ld bytes", sizeof(short));
    printf("\nNULL       | %ld bytes", sizeof(NULL));
    printf("\nbool       | %ld bytes", sizeof(long double));
    printf("\n———————————————————————————————————————————\n");
    return 0;
}
