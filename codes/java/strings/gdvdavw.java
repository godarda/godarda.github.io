// ----------------------------------------------------------------------------------------------------
// Title          : Java implementation of the string split method
// File Name      : gdvdavw.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

class GD
{
    public static void main(String args[])
    {
        String s="Welcome to GoDarda!";
        System.out.println("———————————————————————————————————————————");
        System.out.println("Program to split the given string");
        System.out.println("———————————————————————————————————————————");
        String sarr[]=s.split(" ");
        System.out.println(sarr[0]+"\n"+sarr[1]+"\n"+sarr[2]);
        System.out.println("———————————————————————————————————————————");
    }
}
