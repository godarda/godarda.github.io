// ----------------------------------------------------------------------------------------------------
// Title          : C# program to sort the given numbers in an array
// File Name      : gdywhzb.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

Console.WriteLine("———————————————————————————————————————————");
Console.WriteLine("Program to sort the given numbers in a array");
Console.WriteLine("———————————————————————————————————————————");
int[] arr = new int[] { 23, 34, 5, 4, 1, 99, 58, 14 };  
Array.Sort(arr);
foreach (var i in arr)
{
    Console.WriteLine(i);
}
Console.WriteLine("———————————————————————————————————————————");
