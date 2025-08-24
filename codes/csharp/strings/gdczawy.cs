// ----------------------------------------------------------------------------------------------------
// Title          : C# program to check whether a given string is a palindrome
// File Name      : gdczawy.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

Console.WriteLine("———————————————————————————————————————————");
Console.WriteLine("Program to check string is palindrome | not");
Console.WriteLine("———————————————————————————————————————————");
Console.Write("Enter the string ");
string s = Console.ReadLine()!;
Console.WriteLine("\nLength of a string is " + s.Length);
string r = new string(s.ToCharArray().Reverse().ToArray()!);
Console.WriteLine("\nReverse string is " + r);
if (s == r)
{
    Console.WriteLine("\nString is palindrome");
}
else
{
    Console.WriteLine("\nString is not palindrome");
}
Console.WriteLine("———————————————————————————————————————————");
