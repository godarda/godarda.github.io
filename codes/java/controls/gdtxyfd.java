// ----------------------------------------------------------------------------------------------------
// Title          : Java program to check the given number is positive or negative
// File Name      : gdtxyfd.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import java.util.Scanner;
class GD 
{
    public static void main(String args[])
    {
        int n;
        Scanner sc=new Scanner(System.in);
        System.out.println("———————————————————————————————————————————");
        System.out.println("Program to check the given number is +ve/-ve");
        System.out.println("———————————————————————————————————————————");
        System.out.print("Enter a number ");
        n=sc.nextInt();
        if(n < 0)
        {
            System.out.println("\nEntered number is negative");
        }
        else if(n > 0)
        {
            System.out.println("\nEntered number is positive");
        }
        else
        {
            System.out.println("\nEntered number is zero");
        }
        System.out.println("———————————————————————————————————————————");
    }
}
