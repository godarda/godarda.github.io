// ----------------------------------------------------------------------------------------------------
// Title          : C program to find the range of data types
// File Name      : gdvgrag.c
// Compiled       : gcc (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <stdio.h>
#include <limits.h>
#include <float.h>
int main()
{
    printf("———————————————————————————————————————————");
    printf("\nProgram to find the range of data types");
    printf("\n———————————————————————————————————————————");
    printf("\nChar Bit      | %d", CHAR_BIT);
    printf("\nChar          | %d To %d", CHAR_MIN, CHAR_MAX);
    printf("\nSigned  char  | %d To %d", SCHAR_MIN, SCHAR_MAX);
    printf("\nUnigned char  |  0 To %d", UCHAR_MAX);
    printf("\nSigned  int   | %d To %d", INT_MIN, INT_MAX);
    printf("\nUnigned int   |  0 To %d", INT_MAX);
    printf("\nshort         | %d To %d", SHRT_MIN, SHRT_MAX);
    printf("\nUnigned short |  0 To %d", USHRT_MAX);
    printf("\nlong          | %ld To %ld", LONG_MIN, LONG_MAX);
    printf("\nUnsigned long |  0 To %ld", LONG_MAX);
    printf("\nfloat         | %g To %g", FLT_MIN, FLT_MAX);
    printf("\nSigned  float | %g To %g", -FLT_MIN, -FLT_MAX);
    printf("\ndouble        | %g To %g", DBL_MIN, DBL_MAX);
    printf("\n———————————————————————————————————————————\n");
    return 0;
}
