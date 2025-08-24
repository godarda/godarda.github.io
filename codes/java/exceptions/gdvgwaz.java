// ----------------------------------------------------------------------------------------------------
// Title          : Java program to demonstrate the use of nested try, catch, and finally blocks
// File Name      : gdvgwaz.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

class GD
{
    public static void main(String args[])
    {
        String s=null;
        int n=515, d=0, result=0;
        try
        {
            try
            {
                result=n/d;
            }
            catch(ArithmeticException e)
            {
                System.out.println("Exception caught in the first nested catch block");
            }
            System.out.println("Length: "+s.length());
        }
        catch(ArithmeticException e)
        {
            System.out.println("Exception caught in the first catch block");
        }
        catch(Exception e)
        {
            System.out.println("Exception caught in the third catch block");
        }
    }
}
