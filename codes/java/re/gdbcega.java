// ----------------------------------------------------------------------------------------------------
// Title          : Java program to accept a valid blood group using regex
// File Name      : gdbcega.java
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
        System.out.println("———————————————————————————————————————————");
        System.out.println("Implementation of Regular Expressions");
        System.out.println("———————————————————————————————————————————");
        System.out.print("Enter your blood group ");
        s=sc.nextLine();
        //if(Pattern.matches("([A,B,O]{1}[+,-]{1})|(AB[+,-]{1})",s))
        if(Pattern.matches("(A|B|O|AB)[+,-]{1}",s))
        {
            System.out.println("\nBlood group accepted");
        }
        else
        {
            System.out.println("\nError: No such blood group");
        }
        System.out.println("———————————————————————————————————————————");
    }       
}
