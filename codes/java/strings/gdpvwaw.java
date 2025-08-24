// ----------------------------------------------------------------------------------------------------
// Title          : Java implementation of the equals method
// File Name      : gdpvwaw.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

class GD
{
    public static void main(String args[])
    {
        String s1="HELLO WORLD";
        String s2=s1;
        String s3="Hello World";

        boolean b;
        b=s1.equals(s2);
        System.out.println(b);

        b=s2.equals(s3);
        System.out.println(b);

        b=s1.equalsIgnoreCase(s3);
        System.out.println(b);
    }
}
