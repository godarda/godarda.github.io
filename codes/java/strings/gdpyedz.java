// ----------------------------------------------------------------------------------------------------
// Title          : Java implementation of the contentEquals method
// File Name      : gdpyedz.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

class GD
{
    public static void main(String args[])
    {
        String s1="HELLO";
        String s2="WORLD";
        String s3="HELLO";
        String s4="Hello";

        boolean b=s1.contentEquals(s2);
        System.out.println(b);
        b=s1.contentEquals(s3);
        System.out.println(b);
        b=s1.contentEquals(s4);
        System.out.println(b);
    }
}
