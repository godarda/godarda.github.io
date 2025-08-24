// ----------------------------------------------------------------------------------------------------
// Title          : Java program to perform the division of two numbers
// File Name      : gdgypqx.java
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
        System.out.println("Program to perform the division of two numbers");
        System.out.println("———————————————————————————————————————————");
        System.out.print("Enter the dividend ");
        a=sc.nextFloat();
        System.out.print("Enter the divisor ");
        b=sc.nextFloat();
        System.out.println("Division of two numbers is "+(a/b));
        System.out.println("———————————————————————————————————————————");
    }
}
