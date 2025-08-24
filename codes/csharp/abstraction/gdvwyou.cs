// ----------------------------------------------------------------------------------------------------
// Title          : C# program for Abstract class
// File Name      : gdvwyou.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

abstract class Arithmetic
{
    public int add(int a, int b)
    {
        int c = a + b;
        return c;
    }
    public void display(int c)
    {
        Console.Write("Addition " + c);
    }
}

class Program : Arithmetic
{
    public static void Main(String[] args)
    {
        Program p = new Program();
        int addition = p.add(10, 10);
        p.display(addition);
    }
}
