// ----------------------------------------------------------------------------------------------------
// Title          : Implementation of C# method overloading
// File Name      : gdfzldx.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

Console.WriteLine("Area of Rectangle " + Shape.Rectangle(5, 10));
Console.WriteLine("Area of Rectangle {0}", Shape.Rectangle(3.14, 10));

class Shape
{
    public static int Rectangle(int a, int b)
    {
        return a * b;
    }
    public static double Rectangle(double a, double b)
    {
        return a * b;
    }
}
