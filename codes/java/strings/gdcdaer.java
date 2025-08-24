// ----------------------------------------------------------------------------------------------------
// Title          : Java program to reverse a given string using charAt method
// File Name      : gdcdaer.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import java.util.Scanner;
class GD
{
    public static void main(String args[])
    {
        String s,r="";
        Scanner sc=new Scanner(System.in);
        System.out.println("———————————————————————————————————————————");
        System.out.println("Program to reverse the given string");
        System.out.println("———————————————————————————————————————————");
        System.out.print("Enter the string ");
        s=sc.nextLine();
        for(int i=s.length()-1;i>=0;i--)
        {
            r=r+s.charAt(i);
        }
        System.out.println("\nThe reverse string is "+r);
        System.out.println("———————————————————————————————————————————");
    }
}
