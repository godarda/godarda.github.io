// ----------------------------------------------------------------------------------------------------
// Title          : C program to calculate the area and circumference of a circle
// File Name      : gdfdlyz.c
// Compiled       : gcc (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <stdio.h>
#define PI 3.14
int main()
{
    float R, A, C;
    printf("———————————————————————————————————————————");
    printf("\nProgram to calculate the area and circumference of a circle");
    printf("\n———————————————————————————————————————————");
    printf("\nEnter the radius of a circle ");
    scanf("%f", &R);
    A = PI * R * R;
    printf("\nThe area of a circle is %f ", A);

    C = 2 * PI * R;
    printf("\n\nThe circumference of a circle is %f ", C);
    printf("\n———————————————————————————————————————————\n");
    return 0;
}
