// ----------------------------------------------------------------------------------------------------
// Title          : Java program to print the length of all strings from a given array
// File Name      : gdzyydd.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

class GD
{
    public static void main(String args[])
    {
        System.out.println("———————————————————————————————————————————");
        System.out.println("Program to print strings and its length");
        System.out.println("———————————————————————————————————————————");
        String s[]={"Mouse","Keyboard","Processor","Pen Drive","Joystick"};
        System.out.println("Array contains the following strings"+"\n{");
        
        for(String arr:s)
        System.out.println("   "+arr);
        System.out.println("}\n");
        
        for(int i=0;i<s.length;i++)
        System.out.println(s[i]+" "+s[i].length());
        
        System.out.println("———————————————————————————————————————————");
    }
}
