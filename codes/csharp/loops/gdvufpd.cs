// ----------------------------------------------------------------------------------------------------
// Title          : C# program to find the factorial of a given number
// File Name      : gdvufpd.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

long n, f = 1;
Console.WriteLine("———————————————————————————————————————————");
Console.WriteLine("Program to find the factorial of a number");
Console.WriteLine("———————————————————————————————————————————");
Console.Write("Enter the number ");
n = long.Parse(Console.ReadLine()!);
if(n == 0)
{
    Console.WriteLine("\nFactorial of 0 is 1");
}
else if(n >= 21)
{
    Console.WriteLine("Number should be less than 21");
}
else
{
    f = n;
    for(long i = n - 1; i >= 2; i--)
    {
        f *= i;
    }
    Console.WriteLine("\nFactorial of {0} is {1}", n, f);
}
Console.WriteLine("———————————————————————————————————————————");
