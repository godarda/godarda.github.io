// ----------------------------------------------------------------------------------------------------
// Title          : Java program to print the transpose of a given matrix
// File Name      : gdzapdy.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import java.util.Scanner;
class GD
{
    public static void main(String args[])
    {
        int i,j,m,n;
        Scanner sc=new Scanner(System.in);
        System.out.println("———————————————————————————————————————————");
        System.out.println("Program to find the transpose of a given matrix ");
        System.out.println("———————————————————————————————————————————");
        System.out.print("Enter the number of rows ");
        m=sc.nextInt();
        System.out.print("Enter the number of columns ");
        n=sc.nextInt();
        
        if(m<=0||n<=0||m*n<=0)
        {
            System.out.println("\nEnter the valid number of rows & columns");
        }
        else
        {
            if(m!=n)
            {
                System.out.println("\nGiven matrix is not a square matrix");
            }
            else
            {
                int matrix[][]=new int[m][n];
                System.out.println("Enter the elements of matrix ");
                for(i=0;i<m;i++)
                {
                    for(j=0;j<n;j++)
                    {
                        matrix[i][j]=sc.nextInt();
                    }
                }
                System.out.println("\nEntered matrix is ");
                for(i=0;i<m;i++)
                {
                    for(j=0;j<n;j++)
                    {
                        System.out.print("\t"+matrix[i][j]);
                    }   
                    System.out.println("\t");
                }
                System.out.println("\nTranspose of matrix is ");
                for(i=0;i<m;i++)
                {
                    for(j=0;j<n;j++)
                    {
                        System.out.print("\t"+matrix[j][i]);
                    }   
                    System.out.println("\t");
                }
            }
        }
        System.out.println("———————————————————————————————————————————");
    }
}
