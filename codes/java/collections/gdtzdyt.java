// ----------------------------------------------------------------------------------------------------
// Title          : Java program to perform the Set operations
// File Name      : gdtzdyt.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import java.util.TreeSet;
import java.util.Scanner;
import java.util.Set;

class GD
{
    public static <T> Set<T> Union(Set<T> setA, Set<T> setB)
    {
        Set<T> s = new TreeSet<T>(setA);
        s.addAll(setB);
        return s;
    }

    public static <T> Set<T> Intersection(Set<T> setA, Set<T> setB)
    {
        Set<T> s = new TreeSet<T>();
        for (T x : setA)
            if (setB.contains(x))
                s.add(x);
        return s;
    }

    public static <T> Set<T> Difference(Set<T> setA, Set<T> setB)
    {
        Set<T> s = new TreeSet<T>(setA);
        s.removeAll(setB);
        return s;
    }

    public static <T> Set<T> SymDifference(Set<T> setA, Set<T> setB)
    {
        Set<T> sA;
        Set<T> sB;

        sA = Union(setA, setB);
        sB = Intersection(setA, setB);
        return Difference(sA, sB);
    }

    public static void main(String args[])
    {
        System.out.println("———————————————————————————————————————————");
        System.out.println("Program for the Set operations");
        System.out.println("———————————————————————————————————————————");
        
        TreeSet<Character> set1 = new TreeSet<Character>();
        TreeSet<Character> set2 = new TreeSet<Character>();
        
        Scanner sc = new Scanner(System.in);
        try
        {
            System.out.print("Enter number of elements in Set-1 ");
            int s1 = sc.nextInt();
            for(int i = 1; i <= s1; i++)
            {
                System.out.print("Enter character-"+i+" ");
                char ch = sc.next().charAt(0);
                set1.add(ch);
            }
            
            System.out.print("Enter number of elements in Set-2 ");
            int s2 = sc.nextInt();
            for(int i = 1; i <= s2; i++)
            {
                System.out.print("Enter character-"+i+" ");
                char ch = sc.next().charAt(0);
                set2.add(ch);
            }
            
            System.out.println("———————————————————————————————————————————");
            System.out.println("Result of the Set operations");
            System.out.println("———————————————————————————————————————————");
            System.out.println("Set-1: " + set1);
            System.out.println("Set-2: " + set2);
            System.out.println("Union: " + Union(set1, set2));
            System.out.println("Intersection: " + Intersection(set1, set2));
            System.out.println("Difference (Set-1 - Set-2): " + Difference(set1, set2));
            System.out.println("Difference (Set-2 - Set-1): " + Difference(set2, set1));
            System.out.println("Symmetric Difference: " + SymDifference(set1, set2));
        }
        catch(Exception e)
        {
            System.out.println("Please enter the number only");
        }
    }
}
