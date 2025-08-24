// ----------------------------------------------------------------------------------------------------
// Title          : Implementation of C# Queue class
// File Name      : gdtzzzx.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

using System.Collections;

Queue q = new Queue();
q.Enqueue("Cherry");
q.Enqueue(65655);
q.Enqueue(45588);
q.Enqueue("Apple");

Console.Write("Queue elements: ");
foreach (var s in q)
{
    Console.Write(s + " ");
}

Console.WriteLine("\nFront element: " + q.Peek());
Console.WriteLine("Dequeue: element: " + q.Dequeue());
Console.WriteLine("Front element: " + q.Peek());
Console.WriteLine("Number of elements: " + q.Count);
