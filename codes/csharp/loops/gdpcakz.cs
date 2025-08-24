// ----------------------------------------------------------------------------------------------------
// Title          : C# program to print the star diamond pattern
// File Name      : gdpcakz.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

int i, j;
for (i = 1; i <= 7; i++)
{
    for (j = 1; j <= 7 - i; j++)
    {
        Console.Write(" ");
    }
    for (j = 1; j <= i; j++)
    {
        Console.Write("* ");
    }
    Console.Write("\n");
}
for (i = 6; i >= 1; i--)
{
    for (j = 1; j <= 6 - i; j++)
    {
        Console.Write(" ");
    }
    for (j = 1; j <= i; j++)
    {
        Console.Write(" *");
    }
    Console.Write("\n");
}
