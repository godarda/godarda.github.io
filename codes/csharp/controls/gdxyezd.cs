// ----------------------------------------------------------------------------------------------------
// Title          : C# program to check the given number is positive or negative
// File Name      : gdxyezd.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

int n;
Console.WriteLine("———————————————————————————————————————————");
Console.WriteLine("Program to check the given number is +ve/-ve");
Console.WriteLine("———————————————————————————————————————————");
Console.Write("Enter a number ");
n = Convert.ToInt32(Console.ReadLine());
if (n < 0)
{
    Console.WriteLine("\nEntered number is negative");
}
else if (n > 0)
{
    Console.WriteLine("\nEntered number is positive");
}
else
{
    Console.WriteLine("\nEntered number is zero");
}
Console.WriteLine("———————————————————————————————————————————");
