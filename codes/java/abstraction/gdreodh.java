// ----------------------------------------------------------------------------------------------------
// Title          : How to achieve multiple inheritance in Java using interfaces
// File Name      : gdreodh.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

interface Male
{
    void male();
}

interface Female
{
    void female();
}

interface Category extends Male,Female
{
    void humanBeing();
}

class GD implements Category
{
    public void male() 
    {
        System.out.print("Male + ");
    }
    public void female() 
    {
        System.out.print("Female = ");
    }
    public void humanBeing() 
    {
        System.out.println("We are Human Beings");
    }
    public static void main(String[] args) 
    {
        GD g=new GD();
        g.male();
        g.female();
        g.humanBeing();
    }
}
