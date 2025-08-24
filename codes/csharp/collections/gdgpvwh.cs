// ----------------------------------------------------------------------------------------------------
// Title          : Implementation of C# LinkedList class
// File Name      : gdgpvwh.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

using System.Collections.Generic;

LinkedList<string> ll = new LinkedList<string>();
ll.AddLast("Apple");
ll.AddLast("Orange");
ll.AddLast("Mango");
ll.AddLast("Grapes");
ll.AddLast("Cherry");
ll.AddLast("Apple");
ll.AddFirst("Pineapple");
foreach (string s in ll)
{
    Console.Write(s + " ");
}
Console.WriteLine("\nSize: " + ll.Count);
