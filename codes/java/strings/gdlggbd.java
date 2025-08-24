// ----------------------------------------------------------------------------------------------------
// Title          : How to find the length of a string without using the length method in java
// File Name      : gdlggbd.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

class GD
{
    public static void main(String args[])
    {
        String s = "KODINGWINDOW";
        int length=0;
        for(char c: s.toCharArray())
        {
            length++;    
        } 
        System.out.println("Length of a string is: "+length);  
    }
}
