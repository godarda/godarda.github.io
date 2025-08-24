// ----------------------------------------------------------------------------------------------------
// Title          : Java program to find the length of a given string
// File Name      : gdvdkzc.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import java.util.Scanner;
class GD
{
    public static void main(String args[])
    {
        String s;
        System.out.println("———————————————————————————————————————————");
        System.out.println("Program to find the length of a given string");
        System.out.println("———————————————————————————————————————————");
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter the string ");
        s=sc.nextLine();
        System.out.println("\nEntered string is "+s);
        int l=s.length();
        System.out.println("\nThe length of ("+s +") = "+l);
        System.out.println("———————————————————————————————————————————");
    }
}
