// ----------------------------------------------------------------------------------------------------
// Title          : Java program for Abstract class
// File Name      : gdaalaw.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

abstract class Arithmetic
{
    int add(int a,int b)
    {
        int c=a+b;
        return c;
    }
    void display(int c)
    {
        System.out.println("Addition "+c);
    }
}

class GD extends Arithmetic
{
    public static void main(String[] args) 
    {
        GD g=new GD();
        int addition=g.add(10,10);
        g.display(addition);
    }
}
