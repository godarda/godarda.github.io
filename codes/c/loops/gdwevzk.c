// ----------------------------------------------------------------------------------------------------
// Title          : Find the output of C programs
// File Name      : gdwevzk.c
// Compiled       : gcc (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <stdio.h>
int main()
{
    int a = 5;
    printf("%d\n", ++a + ++a + ++a);
    int b = 5;
    printf("%d %d %d\n", ++b, ++b, ++b);
    return 0;
}
