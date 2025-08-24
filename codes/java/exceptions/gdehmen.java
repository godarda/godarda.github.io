// ----------------------------------------------------------------------------------------------------
// Title          : Java program to handle divide by zero exception
// File Name      : gdehmen.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import java.io.*;
class GD
{
    public static void main(String args[]) 
    {
        System.out.println("———————————————————————————————————————————");
        System.out.println("Program for exceptional handling");
        System.out.println("———————————————————————————————————————————");
        try
        {
            BufferedReader r=new BufferedReader(new InputStreamReader(System.in));
            System.out.print("Enter numerator ");
            int n=Integer.parseInt(r.readLine());
            
            System.out.print("Enter denominator ");
            int d=Integer.parseInt(r.readLine());
            
            System.out.println("Division "+(n/d));
        }
        catch(Exception e)
        {
            System.out.println("Please enter valid input");
        }
        System.out.println("———————————————————————————————————————————");
    }
}
