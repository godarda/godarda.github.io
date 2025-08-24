// ----------------------------------------------------------------------------------------------------
// Title          : C# program to print the prime numbers
// File Name      : gdzttew.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

bool isPrime = true;
Console.WriteLine("———————————————————————————————————————————");
Console.WriteLine("Program to print the prime numbers");
Console.WriteLine("———————————————————————————————————————————");
for (int i = 2; i <= 50; i++)
{
    for (int j = 2; j <= 50; j++)
    {
        if (i != j && i % j == 0)
        {
            isPrime = false;
            break;
        }
    }
    if (isPrime)
    {
        Console.WriteLine(i + " ");
    }
    isPrime = true;
}
Console.WriteLine("———————————————————————————————————————————");
