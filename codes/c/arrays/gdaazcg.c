// ----------------------------------------------------------------------------------------------------
// Title          : Find the output of C programs
// File Name      : gdaazcg.c
// Compiled       : gcc (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <stdio.h>
int main()
{
    int a[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int i = 0, num;
    num = a[++i + a[++i]] + a[++i];
    printf("%d\n", num);
}
