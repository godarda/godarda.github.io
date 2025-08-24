// ----------------------------------------------------------------------------------------------------
// Title          : C# program to handle the IndexOutOfRangeException
// File Name      : gdzuddz.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

using System;
namespace GoDarda
{
    public class Program
    {
        public static void Main(string[] args)
        {
            string[] s = { "Mango", "Pineaple", "Grapes", "Banana", "Apple", "Strawberry" };
            Console.WriteLine("Array Length: " + s.Length);
            Console.WriteLine("First Element: " + s[0]);
            Console.WriteLine("Last Element: " + s[5]);
            Console.WriteLine(s[6]);
        }
    }
}
