// ----------------------------------------------------------------------------------------------------
// Title          : C program to find the min and max of given numbers
// File Name      : gdruyaz.c
// Compiled       : gcc (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <stdio.h>
int main()
{
    int i, n, num, min, max = 0;
    printf("———————————————————————————————————————————");
    printf("\nProgram to find the min/max of given numbers");
    printf("\n———————————————————————————————————————————");
    printf("\nHow many numbers you want to enter ");
    scanf("%d", &n);
    printf("\nEnter %d numbers\n", n);
    scanf("%d", &num);
    min = num;
    if (num >= max)
        max = num;
    for (i = 1; i < n; i++)
    {
        scanf("%d", &num);
        if (num > max)
            max = num;
        if (num < min)
            min = num;
    }
    printf("\nMaximum number %d", max);
    printf("\nMinimum number %d", min);
    printf("\n———————————————————————————————————————————\n");
    return 0;
}
