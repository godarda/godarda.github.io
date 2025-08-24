// ----------------------------------------------------------------------------------------------------
// Title          : C program to demonstrate the use of break and continue statements
// File Name      : gdecgzz.c
// Compiled       : gcc (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <stdio.h>
int main()
{
    for (int i = 0; i < 10; i++)
    {
        if (i == 5)
        {
            break;
        }
        printf("%d\n", i);
    }
    return 0;
}
