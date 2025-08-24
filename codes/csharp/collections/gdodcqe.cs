// ----------------------------------------------------------------------------------------------------
// Title          : Implementation of C# Stack class
// File Name      : gdodcqe.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

using System.Collections;

Stack st = new Stack();
st.Push("Cherry");
st.Push(65655);
st.Push(45588);
st.Push("Apple");

Console.WriteLine("Stack elements: ");
foreach (var s in st)
{
    Console.WriteLine(s);
}
Console.WriteLine("\nPeek element: " + st.Peek());
Console.WriteLine("Pop: element: " + st.Pop());
Console.WriteLine("Peek element: " + st.Peek());
Console.WriteLine("Number of elements: " + st.Count);
