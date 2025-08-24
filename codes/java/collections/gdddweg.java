// ----------------------------------------------------------------------------------------------------
// Title          : Implementation of Java LinkedList class
// File Name      : gdddweg.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import java.util.LinkedList;

class GD 
{
    public static void main(String[] args) 
    {
        //LinkedList class implements the List interface and Deque -> Queue interface
        LinkedList<String> ll=new LinkedList<>();
        ll.add("Apple");
        ll.add("Orange");
        ll.add("Mango");
        ll.add("Grapes");
        ll.add("Cherry");
        ll.add("Apple");
        System.out.println(ll);
        System.out.println("Size: "+ll.size());
    }
}
