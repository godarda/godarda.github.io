// ----------------------------------------------------------------------------------------------------
// Title          : Java program to perform the assignment operations
// File Name      : gdyazyl.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

class GD
{
    public static void main(String args[])
    {
        int a=10,b=50,c;
        System.out.println("———————————————————————————————————————————");
        System.out.println("Program to perform the assignment operations");
        System.out.println("———————————————————————————————————————————");
        System.out.println("Value Of a    | "+a);       //a=10
        System.out.println("Value Of b    | "+b);       //b=50
        System.out.println("Value Of a+=b | "+(a+=b));  //a=a+b=60
        System.out.println("Value Of a-=b | "+(a-=b));  //a=60-10=50
        System.out.println("Value Of a*=b | "+(a*=b));  //a=50*10=500
        System.out.println("Value Of a/=b | "+(a/=b));  //a=500/10=50
        System.out.println("Remainder a%=b| "+(a%=b));  //a=50%10=10
        System.out.println("Value Of a^=b | "+(a^=b));  //a=10
        System.out.println("Value Of a|=b | "+(a|=b));
        System.out.println("Value Of a&=b | "+(a&=b));
        System.out.println("———————————————————————————————————————————");
    }
}
