// ----------------------------------------------------------------------------------------------------
// Title          : Implementation of C# Stack class
// File Name      : gdygygd.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

using System.Collections.Generic;

Stack<string> st = new Stack<string>();
st.Push("Apple");
st.Push("Cherry");
st.Push("Apple");
st.Push("Durian");

Console.WriteLine("Stack elements: ");
foreach (string s in st)
{
    Console.WriteLine(s);
}

Console.WriteLine("\nPeek element: " + st.Peek());
Console.WriteLine("Pop: element: " + st.Pop());
Console.WriteLine("Peek element: " + st.Peek());
Console.WriteLine("Number of elements: " + st.Count);
