// ----------------------------------------------------------------------------------------------------
// Title          : C# program for Multilevel Inheritance
// File Name      : gdkbyga.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

GreenBank gb = new GreenBank();
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
        base.Bonus();
        Console.WriteLine("WhiteBank 1500");
    }
}
class GreenBank : WhiteBank
{
    public void GreenBankBonus()
    {
        base.WhiteBankBonus();
        base.Bonus();
        Console.Write("GreenBank 500");
    }
}
