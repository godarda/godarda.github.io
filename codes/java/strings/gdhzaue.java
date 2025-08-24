// ----------------------------------------------------------------------------------------------------
// Title          : Java program to count the number of holes in a given string and number
// File Name      : gdhzaue.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import java.util.Scanner;
class GD
{
    public static void main(String args[])
    {
        System.out.println("———————————————————————————————————————————");
        System.out.println("Program to find number of holes in a number");
        System.out.println("———————————————————————————————————————————");
        String s="";
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter any number ");
        s=sc.nextLine();

        int count=0,holes=0;
        for(int i=0;i<s.length();i++) 
        {
            if(s.charAt(i)==('0')||s.charAt(i)==('4')||s.charAt(i)==('6')||s.charAt(i)==('9'))
            {
                count++;
                holes=1;
                System.out.println("Hole in  "+s.charAt(i)+" - "+holes);
            }               
            else if(s.charAt(i)==('8'))
            {
                count+=2;
                holes=2;
                System.out.println("Holes in "+s.charAt(i)+" - "+holes);
            }
            else
            {
                holes=0;
                System.out.println("Hole in  "+s.charAt(i)+" - "+holes);
            }
        }
        System.out.println("\nTotal number of holes in given number is "+count);
        System.out.println("———————————————————————————————————————————");
    }
}
