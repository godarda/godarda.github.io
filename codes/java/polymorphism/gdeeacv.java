// ----------------------------------------------------------------------------------------------------
// Title          : Implementation of Java method overloading
// File Name      : gdeeacv.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

class Area
{
    static int rectangle(int a,int b)
    {
        return a*b;
    }
    static double rectangle(double a,double b)
    {
        return a*b;
    }
}

class GD
{
    public static void main(String args[])
    {
        System.out.println("Area of Rectangle "+Area.rectangle(3.14,10.0)); 
        System.out.println("Area of Rectangle "+Area.rectangle(5,10)); 
    }
}
