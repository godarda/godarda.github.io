// ----------------------------------------------------------------------------------------------------
// Title          : Implementation of C# SortedDictionary class
// File Name      : gdvmztp.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

using System.Collections.Generic;

SortedDictionary<long, string> sd = new SortedDictionary<long, string>();
sd.Add(25622348991, "Edward Parkar");
sd.Add(25622348990, "Donald Taylor");
sd.Add(25622348992, "Ryan Bakshi");
sd.Add(25622348989, "James Moore");

foreach (KeyValuePair<long, string> kv in sd)
{
    Console.WriteLine("Account No: {0}, Name: {1}", kv.Key, kv.Value);
}
Console.WriteLine("Size: " + sd.Count);
