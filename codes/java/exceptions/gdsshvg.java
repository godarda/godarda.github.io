// ----------------------------------------------------------------------------------------------------
// Title          : Java program to handle the ArrayIndexOutOfBoundsException
// File Name      : gdsshvg.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

class GD
{
    public static void main(String args[])
    {
        String[] s={"Mango","Pineaple","Grapes","Banana","Apple","Strawberry"};
        System.out.println("Array Length: "+s.length);
        System.out.println("First Element: "+s[0]);
        System.out.println("Last Element: "+s[5]);        
        System.out.println(s[6]);
    }
}
