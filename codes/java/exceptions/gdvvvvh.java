// ----------------------------------------------------------------------------------------------------
// Title          : Java program to demonstrate the use of finally block
// File Name      : gdvvvvh.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

class GD
{
    public static void main(String args[])
    {
        String s=null;
        try
        {
            System.out.println("Length: "+s.length());
        }
        catch(Exception e)
        {
            System.out.println("Exception caught");
        }
        finally
        {
            System.out.println("Finally block always get executed");
        }
    }
}
