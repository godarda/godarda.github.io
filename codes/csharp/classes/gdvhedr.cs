// ----------------------------------------------------------------------------------------------------
// Title          : C# program to demonstrate the use of constructor
// File Name      : gdvhedr.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

Console.WriteLine("———————————————————————————————————————————");
Console.WriteLine("Program to use a constructor");
Console.WriteLine("———————————————————————————————————————————");
Computer c1 = new Computer();
Computer c2 = new Computer("Wireless", "Lenovo", 145221);
c2.display();
GC.Collect();
Console.WriteLine("———————————————————————————————————————————");

public class Computer
{
    public String mouseType = "";
    public String mouseCmp = "";
    public int mouseId;

    public Computer()
    {
        Console.WriteLine("Constructor");
    }
    public Computer(String t, String c, int i)
    {
        mouseType = t;
        mouseCmp = c;
        mouseId = i;
    }
    public void display()
    {
        Console.WriteLine("Mouse Type: " + mouseType + "\nMouse Cmp:  " + mouseCmp + "\nMouse Id:   " + mouseId);
    }
}
