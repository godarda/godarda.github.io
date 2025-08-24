// ----------------------------------------------------------------------------------------------------
// Title          : Implementation of Java ArrayList class
// File Name      : gdsadac.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import java.util.ArrayList;

class GD 
{
    public static void main(String[] args) 
    {
        //ArrayList class implements the List interface
        ArrayList<String> al=new ArrayList<>();
        al.add("Apple");
        al.add("Orange");
        al.add("Mango");
        al.add("Grapes");
        al.add("Cherry");
        al.add("Apple");
        System.out.println(al);
        System.out.println("Size: "+al.size());
    }
}
