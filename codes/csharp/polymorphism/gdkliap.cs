// ----------------------------------------------------------------------------------------------------
// Title          : How to overload the Main() method in C#
// File Name      : gdkliap.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

using System;
namespace GoDarda
{
    class Program
    {
        public static void Main(string s)
        {
            Console.WriteLine("Welcome to " + s);
        }
        public static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
            Main("GoDarda");
        }
    }
}
