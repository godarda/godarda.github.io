// ----------------------------------------------------------------------------------------------------
// Title          : Java program for Hierarchical Inheritance
// File Name      : gdvsmdk.java
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
        System.out.println("WhiteBank 1500");
    }
}
class GreenBank extends Bank
{
    void GreenBankBonus()
    {
        System.out.println("GreenBank 500");
    }
}

class GD 
{
    public static void main(String[] args) 
    {
        WhiteBank wb=new WhiteBank();
        GreenBank gb=new GreenBank();

        wb.Bonus();
        wb.WhiteBankBonus();

        gb.Bonus();
        gb.GreenBankBonus();
    }
}
