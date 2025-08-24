// ----------------------------------------------------------------------------------------------------
// Title          : How to overload the main() method in Java
// File Name      : gdawfyd.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

class GD
{
    public static void main()
    {
        System.out.println("Welcome to GoDarda");
    }
    public static void main(String args[])
    {
        System.out.println("Hello, World!");
        main();
    }
}
