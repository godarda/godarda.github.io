// ----------------------------------------------------------------------------------------------------
// Title          : C progarm for Bubble Sort
// File Name      : gdzxlqf.c
// Compiled       : gcc (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <stdio.h>
int main()
{
    int a[] = {12, 23, -104, -1, 0, 90};
    int n = sizeof(a) / sizeof(a[0]);
    for (int i = 0; i < (n - 1); i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (a[j] > a[j + 1])
            {
                a[j] = a[j] + a[j + 1];
                a[j + 1] = a[j] - a[j + 1];
                a[j] = a[j] - a[j + 1];
            }
        }
    }
    printf("Sorted element(s): ");
    for (int i = 0; i < n; i++)
    {
        printf("%d ", a[i]);
    }
    printf("\n");
    return 0;
}
