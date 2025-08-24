// ----------------------------------------------------------------------------------------------------
// Title          : Implementation of Java LinkedHashSet class
// File Name      : gdsnzag.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import java.util.LinkedHashSet;

class GD 
{
    public static void main(String[] args) 
    {
        //LinkedHashSet class implements the Set interface
        LinkedHashSet<String> lhs=new LinkedHashSet<>();
        lhs.add("Apple");
        lhs.add("Orange");
        lhs.add("Mango");
        lhs.add("Grapes");
        lhs.add("Cherry");
        lhs.add("Apple");
        System.out.println(lhs);
        System.out.println("Size: "+lhs.size());
    }
}
