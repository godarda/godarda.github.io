// ----------------------------------------------------------------------------------------------------
// Title          : C# program for Single Inheritance
// File Name      : gdagvur.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

WhiteBank wb = new WhiteBank();
//wb.Bonus();
wb.WhiteBankBonus();

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
        Console.Write("WhiteBank 1500");
    }
}
