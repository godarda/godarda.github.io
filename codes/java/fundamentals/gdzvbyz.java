// ----------------------------------------------------------------------------------------------------
// Title          : Java program to swap the given numbers
// File Name      : gdzvbyz.java
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
        System.out.println("Program to swap the given numbers");
        System.out.println("———————————————————————————————————————————");
        System.out.print("a = ");
        a=sc.nextFloat();
        System.out.print("b = ");
        b=sc.nextFloat();
        System.out.println("——————————————————————————");
        System.out.println("After swapping...");
        System.out.println("——————————————————————————");
        a+=b; 
        b=a-b;
        a-=b;
        System.out.println("a = "+a+"\nb = "+b);
        System.out.println("———————————————————————————————————————————");
    }       
}
