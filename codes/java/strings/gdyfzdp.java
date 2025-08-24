// ----------------------------------------------------------------------------------------------------
// Title          : Java program to reverse a given string using an array
// File Name      : gdyfzdp.java
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
        System.out.println("———————————————————————————————————————————");
        System.out.println("Program to reverse the given string");
        System.out.println("———————————————————————————————————————————");
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter the string ");
        s=sc.nextLine();
        
        char sarr[]=s.toCharArray();
        int len=0;
        for(char chr:sarr)
        {
            len++;
        }
        System.out.println("\nThe length of a given string is "+len);
        
        for(int i=len-1;i>=0;i--)
        {
            r=r+sarr[i];
        }
        System.out.println("\nThe everse string is "+r);
        System.out.println("———————————————————————————————————————————");
    }
}
