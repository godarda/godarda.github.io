// ----------------------------------------------------------------------------------------------------
// Title          : Implementation of Java ArrayDeque class
// File Name      : gdvpvwx.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import java.util.ArrayDeque;

class GD 
{
    public static void main(String[] args) 
    {
        //ArrayDeque class implements the Queue interface
        ArrayDeque<String> aq=new ArrayDeque<>();
        aq.add("Apple");
        aq.add("Orange");
        aq.add("Mango");
        aq.add("Grapes");
        aq.add("Cherry");
        aq.add("Apple");
        aq.add("Blueberry");
        
        for(String e:aq) 
        { 
            System.out.println(e); 
        }
        System.out.println("Size: "+aq.size());
    }
}
