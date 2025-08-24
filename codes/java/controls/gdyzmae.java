// ----------------------------------------------------------------------------------------------------
// Title          : Java program to check the given number is even or odd
// File Name      : gdyzmae.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import java.util.Scanner;
class GD 
{
    public static void main(String args[])
    {
        int x;
        Scanner sc=new Scanner(System.in);
        System.out.println("———————————————————————————————————————————");
        System.out.println("Program for even-odd test of a given number");
        System.out.println("———————————————————————————————————————————");
        System.out.print("Enter a number ");
        x=sc.nextInt();
        //if((x>>1)<<1==x)
        if(x%2==0)
        {
            System.out.println("\nEntered number is EVEN");
        }
        else
        {
            System.out.println("\nEntered number is ODD");
        }
        System.out.println("———————————————————————————————————————————");
    }
}
