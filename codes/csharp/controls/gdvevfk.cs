// ----------------------------------------------------------------------------------------------------
// Title          : C# program to check the given number is even or odd
// File Name      : gdvevfk.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

int n;
Console.Write("Enter a number ");
n = Convert.ToInt32(Console.ReadLine());
if (n % 2 == 0)
{
    Console.WriteLine(n + " is an EVEN number");
}
else
{
    Console.WriteLine(n + " is an ODD number");
}
