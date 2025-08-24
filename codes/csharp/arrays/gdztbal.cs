// ----------------------------------------------------------------------------------------------------
// Title          : C# implementation of a jagged array
// File Name      : gdztbal.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

Console.WriteLine("———————————————————————————————————————————");
Console.WriteLine("Program to print the jagged array");
Console.WriteLine("———————————————————————————————————————————");
int[][] arr = new int[3][];
arr[0] = new int[] { 23, 34, 5, 99, 58, 14, 59 };
arr[1] = new int[] { 23, 34, 5, 99, 58, 14 };
arr[2] = new int[] { 23, 34, 5, 99 };
for(int i = 0; i < arr.Length; i++)
{
    for(int j = 0; j < arr[i].Length; j++)
    {
        System.Console.Write(arr[i][j] + " ");
    }
    System.Console.WriteLine();
}  
Console.WriteLine("———————————————————————————————————————————");
