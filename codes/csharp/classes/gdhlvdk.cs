// ----------------------------------------------------------------------------------------------------
// Title          : C# implementation of class and object
// File Name      : gdhlvdk.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

Console.WriteLine("———————————————————————————————————————————");
Console.WriteLine("Program to use the class and object");
Console.WriteLine("———————————————————————————————————————————");
Computer c = new Computer();
c.insert("Wireless","Lenovo",145221);
c.display();
Console.WriteLine("———————————————————————————————————————————");

public class Computer
{
    public String mouseType = "";
    public String mouseCmp = "";
    public int mouseId;

    public void insert(String t,String c,int i)
    {
        mouseType = t;
        mouseCmp = c;
        mouseId = i;
    }
    public void display()
    {
        Console.WriteLine("Mouse Type: "+mouseType+"\nMouse Cmp:  "+mouseCmp+"\nMouse Id:   "+mouseId);
    }
}
