// ----------------------------------------------------------------------------------------------------
// Title          : C# implementation of accessors properties
// File Name      : gdagiga.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

Fruit f = new Fruit();
f.FruitName = "Apple";
f.FruitColor = "Red";
Console.WriteLine("———————————————————————————————————————————");
Console.WriteLine("Program to use the accessors properties");
Console.WriteLine("———————————————————————————————————————————");
Console.WriteLine("Fruit Name - " + f.FruitName);
Console.WriteLine("Fruit Color - " + f.FruitColor);
Console.WriteLine(f);
Console.WriteLine("———————————————————————————————————————————");

public class Fruit
{
    private string fname = "";
    private string fcolor = "";
    public string FruitName
    {
        get
        {
            return fname;
        }
        set
        {
            fname = value;
        }
    }

    public string FruitColor
    {
        get
        {
            return fcolor;
        }
        set
        {
            fcolor = value;
        }
    }

    public override string ToString()
    {
        return "Fruit Name - " + FruitName + "\nFruit Color - " + FruitColor;
    }
}
