// ----------------------------------------------------------------------------------------------------
// Title          : C# program to print the Fibonacci series
// File Name      : gdkerds.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

int f1 = 0, f2 = 1, f3 = 0;
Console.WriteLine("———————————————————————————————————————————");
Console.WriteLine("Program to print the Fibonacci series");
Console.WriteLine("———————————————————————————————————————————");
Console.Write("How many elements you want to print ");
int n = Convert.ToInt32(Console.ReadLine());
Console.WriteLine(f1);
Console.WriteLine(f2);
for(int i = 2; i < n; i++)
{
    f3 = f1 + f2;
    Console.WriteLine(f3);
    f1 = f2;
    f2 = f3;
}
Console.WriteLine("———————————————————————————————————————————");
