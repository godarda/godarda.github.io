// ----------------------------------------------------------------------------------------------------
// Title          : C program to perform the Set operations (Union and Intersection)
// File Name      : gdvbrva.c
// Compiled       : gcc (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include <stdio.h>
#define SIZE 50
int S1[SIZE], S2[SIZE], S3[SIZE];
void accept(int S[], int n)
{
    int i;
    for (i = 1; i <= n; i++)
        scanf("%d", &S[i]);
    S[0] = n;
}

void display(int S[])
{
    int n, i;
    n = S[0];
    printf("{ ");
    for (i = 1; i <= n; i++)
        printf("%d ", S[i]);
    printf("}");
}

int ele_pre(int S[], int x)
{
    int n, i;
    n = S[0];
    for (i = 1; i <= n; i++)
        if (S[i] == x)
            return 1;
    return 0;
}

void set_union(int S1[], int S2[])
{
    int n, i, m;
    n = S1[0];
    for (i = 1; i <= n; i++)
        S3[i] = S1[i];
    m = S2[0];
    for (i = 1; i <= m; i++)
        if (!ele_pre(S1, S2[i]))
            S3[++n] = S2[i];
    S3[0] = n;
}

void intersection(int S1[], int S2[])
{
    int n, i, j = 0;
    n = S1[0];
    for (i = 1; i <= n; i++)
        if (ele_pre(S2, S1[i]))
            S3[++j] = S1[i];
    S3[0] = j;
}

int main()
{
    int n;
    printf("———————————————————————————————————————————");
    printf("\nProgram to perform the Set operations");
    printf("\n———————————————————————————————————————————");
    printf("\nHow many elements for Set-1 ");
    scanf("%d", &n);
    printf("\nEnter elements\n");
    accept(S1, n);

    printf("\nHow many elements for Set-2 ");
    scanf("%d", &n);
    printf("\nEnter elements\n");
    accept(S2, n);

    set_union(S1, S2);
    printf("\nS1 U S2 = S3 = ");
    display(S3);

    intersection(S1, S2);
    printf("\nS1 ^ S2 = S3 = ");
    display(S3);
    printf("\n———————————————————————————————————————————\n");
}
