// ----------------------------------------------------------------------------------------------------
// Title          : Java program to handle the OutOfMemoryError exception
// File Name      : gdxyawz.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

class GD
{
    public static void main(String args[])
    {
        int size=Integer.MAX_VALUE;
        System.out.println(size);
        String[] s=new String[size];
    }
}
