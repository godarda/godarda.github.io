// ----------------------------------------------------------------------------------------------------
// Title          : Java program to check whether a given string is a palindrome
// File Name      : gdymyew.java
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
        System.out.println("Program to check string is palindrome | not");
        System.out.println("———————————————————————————————————————————");
        System.out.print("Enter the string ");
        s=sc.nextLine();
        int l=s.length();
        for(int i=l-1;i>=0;i--)
        r=r+s.charAt(i);
        if(s.equals(r))
            System.out.println("\n"+s+" is a palindrome");
        else
            System.out.println("\n"+s+" is a not palindrome");
        System.out.println("———————————————————————————————————————————");
    }
}
