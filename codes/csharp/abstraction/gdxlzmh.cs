// ----------------------------------------------------------------------------------------------------
// Title          : C# program to demonstrate the use of an interface
// File Name      : gdxlzmh.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

Console.WriteLine("———————————————————————————————————————————");
Console.WriteLine("Program to demonstrate the use of interface");
Console.WriteLine("———————————————————————————————————————————");
WhiteBank wb = new WhiteBank();
GreenBank gb = new GreenBank();
gb.credit();
wb.withdraw();
Console.Write("———————————————————————————————————————————");

public interface IBank
{
    void credit();
    void withdraw();
}
public class WhiteBank : IBank
{
    public void credit()
    {
        Console.WriteLine("Your balance is credited in WhiteBank account");
    }
    public void withdraw()
    {
        Console.WriteLine("\nCash withdrew from WhiteBank account");
    }
}
public class GreenBank : IBank
{
    public void credit()
    {
        Console.WriteLine("Your balance is credited in GreenBank account");
    }
    public void withdraw()
    {
        Console.WriteLine("\nCash withdrew from GreenBank account");
    }
}
