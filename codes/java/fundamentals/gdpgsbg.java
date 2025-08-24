// ----------------------------------------------------------------------------------------------------
// Title          : Java program to calculate the area of a circle
// File Name      : gdpgsbg.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import java.util.Scanner;
class GD
{
    public static void main(String args[])
    {
        float r;
        Scanner sc=new Scanner(System.in);
        System.out.println("———————————————————————————————————————————");
        System.out.println("Program to calculate the area of circle ");
        System.out.println("———————————————————————————————————————————");
        System.out.print("Enter the radius of circle ");
        r=sc.nextFloat();
        System.out.println("Area of circle is "+(3.14*r*r));
        System.out.println("Circumference of circle is "+(2*3.14*r));
        System.out.println("———————————————————————————————————————————");
    }
}
