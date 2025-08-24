// ----------------------------------------------------------------------------------------------------
// Title          : Java program to find the unique characters from a given string
// File Name      : gdrmyed.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import java.util.Scanner;
class GD
{
    public static void main(String args[])
    {
        String s1,s2="";
        System.out.println("———————————————————————————————————————————");
        System.out.println("Program to find unique characters");
        System.out.println("———————————————————————————————————————————");
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter the string ");
        s1=sc.nextLine();
        for(int i=0;i<s1.length();i++)
        {
            if(s2.indexOf(s1.charAt(i))==-1)
            {
                s2=s2+s1.charAt(i);
            }
        }
        System.out.println("\nUnique characters "+s2);
        System.out.println("———————————————————————————————————————————");
    }
}
