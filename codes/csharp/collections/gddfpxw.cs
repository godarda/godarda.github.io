// ----------------------------------------------------------------------------------------------------
// Title          : Implementation of C# ArrayList class
// File Name      : gddfpxw.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

using System.Collections;

ArrayList al = new ArrayList();
al.Add("Apple");
al.Add("Banana");
al.Add(50);
al.Add("Cherry");
al.Add("Durian");
al.Add("Apple");
Console.WriteLine("ArrayList: ");
foreach(var fruits in al)
{
    Console.Write(fruits+" ");
}

Console.WriteLine("\n\nThird element: "+al[3]);
Console.WriteLine("Size of ArrayList: "+al.Count);

al.RemoveAt(2); //removed 50
al.Sort();
Console.WriteLine("\nSorted elements: ");
foreach(var fruits in al)
{
    Console.Write(fruits+" ");
}
Console.WriteLine();
