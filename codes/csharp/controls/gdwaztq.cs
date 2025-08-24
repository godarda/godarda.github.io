// ----------------------------------------------------------------------------------------------------
// Title          : C# program to demonstrate the use of goto statement
// File Name      : gdwaztq.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

int n;
Console.Write("Enter a number ");
n = Convert.ToInt32(Console.ReadLine());
if (n % 2 == 0)
{
    goto EVEN;
}
else
{
    goto ODD;
}
EVEN: Console.WriteLine(n + " is an EVEN number");
return 0;
ODD: Console.WriteLine(n + " is an ODD number");
return 0;
