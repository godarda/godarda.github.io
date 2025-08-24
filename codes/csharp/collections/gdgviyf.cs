// ----------------------------------------------------------------------------------------------------
// Title          : Implementation of C# Hashtable class
// File Name      : gdgviyf.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

using System.Collections;

Hashtable ht = new Hashtable();
ht.Add(25622348989, "James Moore");
ht.Add(25622348990, "Donald Taylor");
ht.Add(25622348991, "Edward Parkar");
ht.Add(25622348992, "Ryan Bakshi");

foreach (long key in ht.Keys)
{
    Console.WriteLine("Account No: {0}, Name: {1}", key, ht[key]);
}

ht.Remove(25622348990);
Console.WriteLine("\nAfter removing: ");
foreach (long key in ht.Keys)
{
    Console.WriteLine("Account No: {0}, Name: {1}", key, ht[key]);
}
