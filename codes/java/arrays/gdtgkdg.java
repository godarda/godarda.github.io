// ----------------------------------------------------------------------------------------------------
// Title          : Java program to print the sum of all numbers in a given array
// File Name      : gdtgkdg.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

class GD
{
    public static void main(String args[])
    {
        double sum=0;
        double []a={100,15,15.15,40,45.99};
        for(int i=0;i<a.length;i++)
        {
            sum=sum+a[i];
        }
        System.out.println("The addition of array is = "+sum);
    }
}
