// ----------------------------------------------------------------------------------------------------
// Title          : Java program to find the min and max number from a given array
// File Name      : gdzeyvr.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

class GD
{
    public static void main(String args[])
    {
        System.out.println("———————————————————————————————————————————");
        System.out.println("Implementation of Java arrays ");
        System.out.println("———————————————————————————————————————————");
        double []a={100,15,15.15,400,45.99};
        System.out.println("Array contains the following numbers"+"\n{");
        for(double arr:a)
            System.out.println("   "+arr);
            double sum=0;
            for(int i=0;i<a.length;i++)
            {
                sum=sum+a[i];
            }
        System.out.println("}\nThe addition of array is = "+sum);
        double max=a[0];
        double min=max;
        for(int i=0;i<a.length;i++)
        {
            if(a[i]>max)
                max=a[i];
            if(a[i]<min)
                min=a[i];
        }
        System.out.println("\nThe max number from a given array is "+max);
        System.out.println("\nthe min number from a given array is "+min);
        System.out.println("———————————————————————————————————————————");
    }
}
