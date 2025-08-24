// ----------------------------------------------------------------------------------------------------
// Title          : C# program for Hybrid Inheritance (Multilevel and Hierarchical)
// File Name      : gddsxvh.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

GreenBank gb = new GreenBank();
gb.GreenBankBonus();
gb.WhiteBankBonus();

PinkBank pb = new PinkBank();
pb.PinkBankBonus();
pb.WhiteBankBonus();

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
        base.Bonus();
        Console.WriteLine("GreenBank 500");
    }
}
class PinkBank : WhiteBank
{
    public void PinkBankBonus()
    {
        base.Bonus();
        Console.WriteLine("PinkBank 1000");
    }
}
