// ----------------------------------------------------------------------------------------------------
// Title          : C# program for complex numbers operations
// File Name      : gdcaygv.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

Complex c1 = new Complex(4, 5);
Complex c2 = new Complex(2, 6);
Complex add = c1 + c2;
Complex sub = c1 - c2;
Complex mul = c1 * c2;
Complex div = c1 / c2;
Console.WriteLine("———————————————————————————————————————————");
Console.WriteLine("Implementation of complex numbers operations");
Console.WriteLine("———————————————————————————————————————————");
Console.WriteLine("1st complex number {0}", c1);
Console.WriteLine("2nd complex number {0}", c2);
Console.WriteLine("\nAddition {0}", add);
Console.WriteLine("\nSubtraction {0}", sub);
Console.WriteLine("\nMultiplication {0}", mul);
Console.WriteLine("\nDivision {0}", div);
Console.WriteLine("———————————————————————————————————————————");

public struct Complex
{
    public double real;
    public double imaginary;
    public Complex(double real, double imaginary)
    {
        this.real = real;
        this.imaginary = imaginary;
    }

    public static Complex operator + (Complex c1, Complex c2)
    {
        return new Complex(c1.real + c2.real, c1.imaginary + c2.imaginary);
    }

    public static Complex operator - (Complex c1, Complex c2)
    {
        return new Complex(c1.real - c2.real, c1.imaginary - c2.imaginary);
    }

    public static Complex operator * (Complex c1, Complex c2)
    {
        return new Complex(((c1.real) * (c2.real)) - ((c1.imaginary) * (c2.imaginary)), ((c1.real) * (c2.imaginary)) + ((c2.real) * (c1.imaginary)));
    }

    public static Complex operator / (Complex c1, Complex c2)
    {
        double a = (((c1.real) * (c2.real)) + ((c1.imaginary) * (c2.imaginary))) / (Math.Pow(c2.real, 2) + Math.Pow(c2.imaginary, 2));
        double b = (((c2.real) * (c1.imaginary)) - ((c1.real) * (c2.imaginary))) / (Math.Pow(c2.real, 2) + Math.Pow(c2.imaginary, 2));
        return new Complex(a, b);
    }

    public override string ToString()
    {
        if (imaginary >= 0)
        {
            return (String.Format("{0}+{1}i", real, imaginary));
        }
        else
        {
            return (String.Format("{0}{1}i", real, imaginary));
        }
    }
}
