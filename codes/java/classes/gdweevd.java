// ----------------------------------------------------------------------------------------------------
// Title          : Java implementation of a call by value
// File Name      : gdweevd.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

class GD
{
    public static int add(int a,int b)
    {
        a=100;
        b=100;
        int c=a+b;
        return c;
    }
    public static void main(String args[])
    {
        int a=20,b=10,c;
        c=a+b;
        add(a,b);
        System.out.println(a+b);
    }
}
