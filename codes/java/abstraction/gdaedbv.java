// ----------------------------------------------------------------------------------------------------
// Title          : How to achieve multiple inheritance in Java using interfaces and default methods
// File Name      : gdaedbv.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

interface WhiteBank
{
    default void bonus()
    {
        System.out.println("WhiteBank Festival Bonus: 500");
    }
}
interface GreenBank
{
    default void gift()
    {
        System.out.println("GreenBank Festival Gift: 1000");
    }
}
class GD implements WhiteBank, GreenBank
{
    public static void main(String args[])
    {
        GD g=new GD();
        g.bonus();
        g.gift();
    }
}
