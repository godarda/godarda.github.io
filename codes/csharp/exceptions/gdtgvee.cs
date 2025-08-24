// ----------------------------------------------------------------------------------------------------
// Title          : C# program to catch all the exceptions using Exception class
// File Name      : gdtgvee.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

int a = 1, b = 0;
try
{
    try
    {
        Console.WriteLine(a / b);
    }
    catch (Exception e)
    {
        Console.WriteLine("First Exception: " + e.ToString());
    }
    string s = null;
    Console.WriteLine(s.Length);

}
catch (Exception e)
{
    Console.WriteLine("Second Exception: " + e.ToString());
}
