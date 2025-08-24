// ----------------------------------------------------------------------------------------------------
// Title          : Implementation of Java TreeSet class
// File Name      : gdrezey.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import java.util.TreeSet;

class GD 
{
    public static void main(String[] args) 
    {
        //TreeSet class implements the NavigableSet -> SortedSet -> Set interface
        TreeSet<String> ts=new TreeSet<>();
        ts.add("Apple");
        ts.add("Orange");
        ts.add("Mango");
        ts.add("Grapes");
        ts.add("Cherry");
        ts.add("Apple");
        
        System.out.println(ts);
        System.out.println("Size: "+ts.size());
    }
}
