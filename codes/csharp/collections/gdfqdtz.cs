// ----------------------------------------------------------------------------------------------------
// Title          : Implementation of C# HashSet class
// File Name      : gdfqdtz.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

using System.Collections.Generic;

HashSet<string> hs = new HashSet<string>();
hs.Add("Cherry");
hs.Add("Apple");
hs.Add("Orange");
hs.Add("Mango");
hs.Add("Grapes");
hs.Add("Cherry");
hs.Add("Apple");
hs.Add("Pineapple");
hs.Add("Cherry");

foreach (string s in hs)
{
    Console.Write(s + " ");
}
Console.WriteLine("\nSize: " + hs.Count);
