// ----------------------------------------------------------------------------------------------------
// Title          : C# program to demonstrate the use of regular expressions
// File Name      : gdvpoef.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

using System.Text.RegularExpressions;

Console.WriteLine("———————————————————————————————————————————");
Console.WriteLine("C# program for the regular expressions");
Console.WriteLine("———————————————————————————————————————————");
string s = "ABC DEF 123 456 789";
Match m = Regex.Match(s, @"\d+");
if (m.Success)
{
    Console.WriteLine(m.Value);
    Console.WriteLine("Value " + m.Value);
    Console.WriteLine("Length " + m.Length);
    Console.WriteLine("Index " + m.Index);
}
else
{
    Console.WriteLine("Not Matched");
}

if (Regex.IsMatch(s, "abc..", RegexOptions.IgnoreCase))
{
    Console.WriteLine("Matched");
}
else
{
    Console.WriteLine("Not Matched");
}
Console.WriteLine(IsValid("Hello 123456789"));
Console.WriteLine(IsValid(":)"));
Console.WriteLine("———————————————————————————————————————————");

static bool IsValid(string s)
{
    return Regex.IsMatch(s, @"^[a-zA-Z0-9 ]*$");
}
