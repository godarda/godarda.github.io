// ----------------------------------------------------------------------------------------------------
// Title          : Java program to reverse a given string using the reverse method
// File Name      : gdvvbei.java
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
        Scanner sc=new Scanner(System.in);
        System.out.println("———————————————————————————————————————————");
        System.out.println("Program to reverse the given string");
        System.out.println("———————————————————————————————————————————");
        System.out.print("Enter the string ");
        s=sc.nextLine();
        String r=new StringBuffer(s).reverse().toString();
        System.out.println("\nThe reverse string is "+r);
        System.out.println("———————————————————————————————————————————");
    }
}
