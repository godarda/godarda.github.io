// ----------------------------------------------------------------------------------------------------
// Title          : Java implementation of Scanner close method
// File Name      : gdwqzgy.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import java.util.Scanner;
class GD
{
    public void action()
    {
        stringScanner();
        intScanner();
    }
    
    public void stringScanner()
    {
        String s="";
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter the string ");
        if(sc.hasNext())
        {
            s=sc.nextLine();
        }
        sc.close();
        System.out.println("\nString "+s);
    }
    
    public void intScanner()
    {
        int n=0;
        Scanner sc=new Scanner(System.in);
        System.out.print("\nEnter the number ");
        if(sc.hasNext())
        {
            n=sc.nextInt();
        }
        sc.close();
        System.out.println("\nNumber "+n);
    }
    
    public static void main(String args[])
    {
        System.out.println("———————————————————————————————————————————");
        System.out.println("Java implementation of Scanner close method");
        System.out.println("———————————————————————————————————————————");
        GD g=new GD();
        g.stringScanner();
        g.intScanner();
        System.out.println("———————————————————————————————————————————");
    }
}
