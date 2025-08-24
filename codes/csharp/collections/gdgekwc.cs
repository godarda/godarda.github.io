// ----------------------------------------------------------------------------------------------------
// Title          : Implementation of C# Dictionary class
// File Name      : gdgekwc.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

using System.Collections.Generic;

Dictionary<long, string> dict = new Dictionary<long, string>();
dict.Add(25622348989, "James Moore");
dict.Add(25622348990, "Donald Taylor");
dict.Add(25622348991, "Edward Parkar");
dict.Add(25622348992, "Ryan Bakshi");

foreach (KeyValuePair<long, string> kv in dict)
{
    Console.WriteLine("Account No: {0}, Name: {1}", kv.Key, kv.Value);
}
Console.WriteLine("Size: " + dict.Count);
