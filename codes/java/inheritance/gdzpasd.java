// ----------------------------------------------------------------------------------------------------
// Title          : Java program for Single Inheritance
// File Name      : gdzpasd.java
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

class GD 
{
    public static void main(String[] args) 
    {
        WhiteBank wb=new WhiteBank();
        wb.Bonus();
        wb.WhiteBankBonus();
    }
}
