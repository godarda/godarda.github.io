// ----------------------------------------------------------------------------------------------------
// Title          : Java program to perform the string operations
// File Name      : gdoazqw.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

class GD
{
    public static void main(String args[])
    {
        String s="Hello World";
        System.out.println("———————————————————————————————————————————");
        System.out.println("Program to perform the string operations");
        System.out.println("———————————————————————————————————————————");
        System.out.println("Main string | "+s);
        System.out.println("———————————————————————————————————————————");
        System.out.println("Length of string      | "+s.length());
        System.out.println("Lowercase of string   | "+s.toLowerCase());
        System.out.println("Uppercase of string   | "+s.toUpperCase());
        char c=s.charAt(6);
        System.out.println("Char at 6th position  | "+(c));
        System.out.println("Index position of W   | "+s.indexOf('W'));
        System.out.println("Matching substring ld | "+s.matches("(.*)ld(.*)"));
        System.out.println("Is string start with A| "+s.startsWith("A"));
        System.out.println("Replace space by *    | "+s.replace(' ','*'));
        System.out.println("From 3rd position     | "+s.substring(3));
        System.out.println("Dispaly from e to r   | "+s.subSequence(1,9));
        System.out.println("Hash code for string  | "+s.hashCode());
        System.out.println("———————————————————————————————————————————");
    }
}
