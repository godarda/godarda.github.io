// ----------------------------------------------------------------------------------------------------
// Title          : Java program to demonstrate the use of constructor
// File Name      : gdkogzp.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

class GD
{
    int i=0;
    public GD()
    {
        i=i+1;
        System.out.println(i);
    }
    public static void main(String args[])
    {
        GD g=new GD();
        GD k1=new GD();
        GD k2=new GD();
    }
}
