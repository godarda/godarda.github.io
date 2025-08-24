// ----------------------------------------------------------------------------------------------------
// Title          : Implementation of Java Regular Expressions
// File Name      : gdwdgez.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import java.util.*;
import java.util.regex.*;
class GD
{
    public static void main(String args[])
    {
        String s;
        Scanner sc=new Scanner(System.in);
        System.out.println("____________________________________");
        System.out.println("Implementation of Regular Expression");
        System.out.println("____________________________________");
        System.out.print("Enter a number ");
        s=sc.nextLine();
        if(Pattern.matches("\\d*",s))
        {
            System.out.println("\nNumber accepted");
        }
        else
        {
            System.out.println("\nError: number unacceptable");
        }
        System.out.println("____________________________________");
    }       
}
