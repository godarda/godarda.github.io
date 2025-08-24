// ----------------------------------------------------------------------------------------------------
// Title          : C# program for Hierarchical Inheritance
// File Name      : gdvfzfg.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

WhiteBank wb = new WhiteBank();
GreenBank gb = new GreenBank();

wb.Bonus();
wb.WhiteBankBonus();

gb.Bonus();
gb.GreenBankBonus();

class Bank
{
    public void Bonus()
    {
        Console.Write("Festival Bonus: ");
    }
}
class WhiteBank : Bank
{
    public void WhiteBankBonus()
    {
        Console.WriteLine("WhiteBank 1500");
    }
}
class GreenBank : Bank
{
    public void GreenBankBonus()
    {
        Console.Write("GreenBank 500");
    }
}
