// ----------------------------------------------------------------------------------------------------
// Title          : Implementation of Java HashSet class
// File Name      : gdsftmv.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import java.util.HashSet;
import java.util.Iterator;

class GD 
{
    public static void main(String[] args) 
    {
        //HashSet class implements the Set interface
        HashSet<String> hs=new HashSet<>();
        hs.add("Apple");
        hs.add("Orange");
        hs.add("Mango");
        hs.add("Grapes");
        hs.add("Cherry");
        hs.add("Apple");
        Iterator itr=hs.iterator();
        while(itr.hasNext())
        {
            System.out.println(itr.next());
        }
        System.out.println("Size: "+hs.size());
    }
}
