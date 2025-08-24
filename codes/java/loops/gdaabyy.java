// ----------------------------------------------------------------------------------------------------
// Title          : Java program to find the factorial of a given number
// File Name      : gdaabyy.java
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
        System.out.println("Program to find the factorial of a given number");
        System.out.println("———————————————————————————————————————————");
        long i,fact=1,n;
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter the number ");
        n=sc.nextInt();
        if(n>20||n<0)
        {
            System.out.println("OOP's can't find "+n+"!");
        }
        else
        {
            for(i=1;i<=n;i++)
            {
                fact=fact*i;
            }
            System.out.println(n+"! = "+fact);
        }
        System.out.println("———————————————————————————————————————————");
    }
}
