// ----------------------------------------------------------------------------------------------------
// Title          : C# program to demonstrate the use of namespace
// File Name      : gdgzuze.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

using Circle;
using Rectangle;

Circle.Shape s1 = new Circle.Shape();
Rectangle.Shape s2 = new Rectangle.Shape();
Console.WriteLine("———————————————————————————————————————————");
Console.WriteLine("Program to demonstrate the use of namespace");
Console.WriteLine("———————————————————————————————————————————");
Console.WriteLine("Area of a circle is " + s1.Area(5));
Console.WriteLine("Area of a rectangle is " + s2.Area(5, 2));
Console.WriteLine("———————————————————————————————————————————");

namespace Circle
{
    public class Shape
    {
        public static float PI = 3.14F;
        public float Area(float r)
        {
            float area = PI * r * r;
            return area;
        }
    }
}

namespace Rectangle
{
    public class Shape
    {
        public float Area(float l, float w)
        {
            float area = l * w;
            return area;
        }
    }
}
