// ----------------------------------------------------------------------------------------------------
// Title          : Java program to handle the StringIndexOutOfBoundsException
// File Name      : gdpdygw.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

class GD
{
    public static void main(String args[])
    {
        String s="Hello, World!";
        System.out.println("Length: "+s.length());
        System.out.println("0th Character: "+s.charAt(0));
        System.out.println("14th Character: "+s.charAt(14));
    }
}
