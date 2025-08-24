// ----------------------------------------------------------------------------------------------------
// Title          : C# program to demonstrate the use of finally blocks
// File Name      : gdkzaae.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

string s = null;
try
{
    Console.WriteLine("Length: " + s.Length);
}
catch (Exception e)
{
    Console.WriteLine("Exception caught");
}
finally
{
    Console.WriteLine("Finally block is always get executed");
}
