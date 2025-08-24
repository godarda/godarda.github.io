// ----------------------------------------------------------------------------------------------------
// Title          : Implementation of Java method overriding
// File Name      : gdazeyz.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

class Fruit
{
    void cutting()
    {
        System.out.print("Cutting Fruit ");
    }  
}

class Mango extends Fruit
{
    void cutting()
    {
        super.cutting(); //invokes the super class method
        System.out.println("Mango");
    }
}
class Apple extends Fruit
{
    void cutting()
    {
        super.cutting(); //invokes the super class method
        System.out.println("Apple");
    }
}

class GD extends Fruit
{
    public static void main(String args[])
    {
        Fruit m=new Mango(); //Mango object
        m.cutting();
        Fruit a=new Apple(); //Apple object
        a.cutting();
    }
}
