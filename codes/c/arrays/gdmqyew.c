// ----------------------------------------------------------------------------------------------------
// Title          : C program to find the min and max number from a given array
// File Name      : gdmqyew.c
// Compiled       : gcc (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <stdio.h>
int main()
{
    int min, max;
    int arr[5] = {100, 15, 8, 45, 93};
    min = max = arr[0];
    for (int i = 0; i < 5; i++)
    {
        if (arr[i] > max)
            max = arr[i];
        if (arr[i] < min)
            min = arr[i];
    }
    printf("The max number from a given array is %d ", max);
    printf("The min number from a given array is %d ", min);
    return 0;
}
