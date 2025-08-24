// ----------------------------------------------------------------------------------------------------
// Title          : Implementation of C# List class
// File Name      : gdrlbiw.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

using System.Collections.Generic;

List<string> li = new List<string>();
li.Add("Apple");
li.Add("Orange");
li.Add("Mango");
li.Add("Grapes");
li.Add("Cherry");
li.Add("Apple");

li.Insert(0, "Pineapple");

for (int i = 0; i < li.Count; i++)
{
    Console.Write(li[i] + " ");
}
Console.WriteLine("\nSize: " + li.Count);
Console.WriteLine("Capacity: " + li.Capacity);
