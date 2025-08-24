// ----------------------------------------------------------------------------------------------------
// Title          : Java program for Hybrid Inheritance (Multilevel and Hierarchical)
// File Name      : gddfehy.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

class Bank
{
    void Bonus()
    {
        System.out.print("Festival Bonus: ");
    }  
}
class WhiteBank extends Bank
{
    void WhiteBankBonus()
    {
        super.Bonus();
        System.out.println("WhiteBank 1500");
    }
}
class GreenBank extends WhiteBank
{
    void GreenBankBonus()
    {
        super.Bonus();
        System.out.println("GreenBank 500");
    }
}
class PinkBank extends WhiteBank
{
    void PinkBankBonus()
    {
        super.Bonus();
        System.out.println("PinkBank 1000");
    }
}

class GD 
{
    public static void main(String[] args) 
    {
        GreenBank gb=new GreenBank();
        gb.GreenBankBonus();
        gb.WhiteBankBonus();
        
        PinkBank pb=new PinkBank();
        pb.PinkBankBonus();
        pb.WhiteBankBonus();
    }
}
