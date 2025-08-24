// ----------------------------------------------------------------------------------------------------
// Title          : C program to print the current date and time
// File Name      : gdvzlki.c
// Compiled       : gcc (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <stdio.h>
#include <time.h>
int main()
{
    time_t t;
    time(&t);
    printf("Current Date and Time is %s", ctime(&t));
    return 0;
}
