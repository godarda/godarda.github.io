// ----------------------------------------------------------------------------------------------------
// Title          : C# program to print the Fibonacci series using recursion
// File Name      : gdazxvw.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

Console.WriteLine("———————————————————————————————————————————");
Console.WriteLine("Program to print the Fibonacci series");
Console.WriteLine("———————————————————————————————————————————");
Console.Write("How many elements you want to print ");
int n = Convert.ToInt32(Console.ReadLine());
for (int i = 0; i < n; i++)
{
    int F = Fibonacci(i);
    Console.WriteLine(F);
}
Console.WriteLine("———————————————————————————————————————————");

static int Fibonacci(int n)
{
    if ((n == 0) || (n == 1))
    {
        return n;
    }
    else
    {
        return Fibonacci(n - 1) + Fibonacci(n - 2);
    }
}
