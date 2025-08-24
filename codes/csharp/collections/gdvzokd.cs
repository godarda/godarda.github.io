// ----------------------------------------------------------------------------------------------------
// Title          : Implementation of C# Queue class
// File Name      : gdvzokd.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

using System.Collections.Generic;

Queue<string> q = new Queue<string>();
q.Enqueue("Apple");
q.Enqueue("Cherry");
q.Enqueue("Apple");
q.Enqueue("Durian");

Console.Write("Queue elements: ");
foreach (string s in q)
{
    Console.Write(s + " ");
}

Console.WriteLine("\nFront element: " + q.Peek());
Console.WriteLine("Dequeue: element: " + q.Dequeue());
Console.WriteLine("Front element: " + q.Peek());
Console.WriteLine("Number of elements: " + q.Count);
