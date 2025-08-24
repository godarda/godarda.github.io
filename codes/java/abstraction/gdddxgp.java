// ----------------------------------------------------------------------------------------------------
// Title          : Java program for Interface
// File Name      : gdddxgp.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

interface Operations
{
    interface add
    {
        void add(int x,int y);
    }
    interface sub
    {
        void sub(int x,int y);
    }
}

class GD implements Operations
{
    void add(int x,int y) 
    {
        System.out.println("Addition "+(x+y));
    }
    void sub(int x,int y) 
    {
        System.out.println("Subtraction "+(x-y));
    }
    public static void main(String[] args) 
    {
        GD g=new GD();
        g.add(10,20);
        g.sub(20,10);
    }
}
