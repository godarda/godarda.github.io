// ----------------------------------------------------------------------------------------------------
// Title          : Java program to perform the boolean operations
// File Name      : gdnozez.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

class GD
{
    public static void main(String args[])
    {
        boolean a=true,b=false;
        System.out.println("———————————————————————————————————————————");
        System.out.println("Program to perform the boolean operations");
        System.out.println("———————————————————————————————————————————");
        System.out.println(a+" |  "+b+"\t| "+(a|b));
        System.out.println(a+" &  "+b+"\t| "+(a&b));
        System.out.println(a+" ^  "+b+"\t| "+(a^b));
        System.out.println(a+" || "+b+"\t| "+(a||b));
        System.out.println(a+" && "+b+"\t| "+(a&&b));
        System.out.println(a+" == "+b+"\t| "+(a==b));
        System.out.println(a+" != "+b+"\t| "+(a!=b));
        System.out.println("!("+a+" || "+b+")| "+!(a||b));
        System.out.println("———————————————————————————————————————————");
    }
}
