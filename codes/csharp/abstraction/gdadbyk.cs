// ----------------------------------------------------------------------------------------------------
// Title          : How to achieve Multiple Inheritance in C# using interfaces
// File Name      : gdadbyk.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

Bank b=new Bank();
b.WhiteBankBonus();
b.GreenBankBonus();

interface IWhiteBank
{
    void WhiteBankBonus();
}
interface IGreenBank
{
    void GreenBankBonus();
}
class Bank : IWhiteBank, IGreenBank
{
    public void WhiteBankBonus()
    {
        Console.WriteLine("WhiteBank Festival Bonus: 1500");
    }
    public void GreenBankBonus()
    {
        Console.Write("GreenBank Festival Bonus: 500");
    }
}
