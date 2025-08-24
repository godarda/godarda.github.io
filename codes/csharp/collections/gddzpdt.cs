// ----------------------------------------------------------------------------------------------------
// Title          : Implementation of C# SortedSet class
// File Name      : gddzpdt.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

using System.Collections.Generic;

SortedSet<string> ss = new SortedSet<string>();
ss.Add("Cherry");
ss.Add("Apple");
ss.Add("Orange");
ss.Add("Mango");
ss.Add("Grapes");
ss.Add("Cherry");
ss.Add("Apple");
ss.Add("Pineapple");
ss.Add("Cherry");

foreach (string s in ss)
{
    Console.Write(s + " ");
}
Console.WriteLine("\nSize: " + ss.Count);
