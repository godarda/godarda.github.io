// ----------------------------------------------------------------------------------------------------
// Title          : Java program to print the star pyramid patterns
// File Name      : gdwzoda.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

class GD
{
    public static void main(String args[])
    {
        int i,j;
        for(i=1;i<=10;i++)
        {
            for(j=1;j<=i;j++)
            {
                System.out.print("*");
            }
            System.out.println("");
        }

        /*
        for(i=10;i>=1;i--)
        {
            for(j=10;j>=i;j--)
            {
                System.out.print((char)42);
            }
            System.out.println("");
        }
        */
    }
}
