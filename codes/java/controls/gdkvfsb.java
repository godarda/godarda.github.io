// ----------------------------------------------------------------------------------------------------
// Title          : Java program to check the equality of given numbers
// File Name      : gdkvfsb.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import java.util.Scanner;
class GD 
{
    public static void main(String args[])
    {
        float a,b;
        Scanner sc=new Scanner(System.in);
        System.out.println("———————————————————————————————————————————");
        System.out.println("Program to check the equality of given numbers");
        System.out.println("———————————————————————————————————————————");
        System.out.print("\nEnter the 1st number ");
        a=sc.nextFloat();
        System.out.print("\nEnter the 2nd number ");
        b=sc.nextFloat();
        if(a>b)
            System.out.println("\n"+a+" is greater than "+b);
        else if(a<b)
            System.out.println("\n"+a+" is less than "+b);
        else
            System.out.println("\n"+a+" is equal to "+b);
        System.out.println("———————————————————————————————————————————");
    }
}
