// ----------------------------------------------------------------------------------------------------
// Title          : C# program to perform the string operations
// File Name      : gdyyfzg.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

string s1 = "HELLO WORLD";
string s2 = "hello world";
Console.WriteLine("———————————————————————————————————————————");
Console.WriteLine("Program to perform the string operations");
Console.WriteLine("———————————————————————————————————————————");
Console.WriteLine("Length of string is " + s1.Length);
string r = new string(s1.ToCharArray().Reverse().ToArray());
Console.WriteLine("\nReverse string is " + r);
Console.WriteLine("\nUppercase string is " + s2.ToUpper());
Console.WriteLine("\nLowercase string is " + s1.ToLower());
if (s1.CompareTo(s2) == 0)
{
    Console.WriteLine("\nStrings are equal");
}
else
{
    Console.WriteLine("\nStrings are not equal");
}
if (s1 == r)
{
    Console.WriteLine("\n{0} String is palindrome", s1);
}
else
{
    Console.WriteLine("\n{0} String is not palindrome", s1);
}
Console.WriteLine("\nSubstring - " + s1.Substring(7));
Console.WriteLine("\nString replaced - " + s1.Replace("WORLD", "Programmers"));
Console.WriteLine("\nIndexOf string - " + s1.IndexOf("W"));
Console.WriteLine("———————————————————————————————————————————");
