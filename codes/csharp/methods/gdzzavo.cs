// ----------------------------------------------------------------------------------------------------
// Title          : C# program for addition of two numbers using a method
// File Name      : gdzzavo.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

Arithmetic a = new Arithmetic();
Console.Write("Addition: " + a.addition(10, 20));

class Arithmetic
{
    public int addition(int a, int b)
    {
        int sum = a + b;
        return sum;
    }
}
