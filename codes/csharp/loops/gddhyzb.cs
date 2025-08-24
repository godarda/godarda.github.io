// ----------------------------------------------------------------------------------------------------
// Title          : C# program to print the Armstrong numbers
// File Name      : gddhyzb.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

int num, r, sum, temp, ul;
Console.WriteLine("———————————————————————————————————————————");
Console.WriteLine("Program to print the Armstrong numbers");
Console.WriteLine("———————————————————————————————————————————");
Console.Write("Enter the upper limit range ");
ul = Convert.ToInt32(Console.ReadLine());
Console.Write("\nArmstrong numbers are\n");
for (num = 1; num <= ul; num++)
{
    temp = num;
    sum = 0;
    while (temp != 0)
    {
        r = temp % 10;
        temp = temp / 10;
        sum = sum + (r * r * r);
    }
    if (sum == num)
    {
        Console.WriteLine("{0} ", num);
    }
}
Console.WriteLine("———————————————————————————————————————————");
