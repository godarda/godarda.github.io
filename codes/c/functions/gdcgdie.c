// ----------------------------------------------------------------------------------------------------
// Title          : C program for the Tower of Hanoi
// File Name      : gdcgdie.c
// Compiled       : gcc (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <stdio.h>
int main()
{
    int n;
    void towers(int n, char source, char destination, char auxiliary);
    printf("———————————————————————————————————————————");
    printf("\nProgram for the Tower of Hanoi");
    printf("\n———————————————————————————————————————————");
    printf("\nEnter Number of Disks ");
    scanf("%d", &n);
    towers(n, 'A', 'B', 'C');
    printf("\n———————————————————————————————————————————\n");
    return 0;
}
void towers(int n, char source, char destination, char auxiliary)
{
    if (n == 1)
    {
        printf("\nMove disk 1 from peg %c to peg %c", source, destination);
        return;
    }
    towers(n - 1, source, auxiliary, destination);
    printf("\nMove disk %d from peg %c to peg %c", n, source, destination);
    towers(n - 1, auxiliary, destination, source);
}
