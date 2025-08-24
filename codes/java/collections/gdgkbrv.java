// ----------------------------------------------------------------------------------------------------
// Title          : Implementation of Java PriorityQueue class
// File Name      : gdgkbrv.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import java.util.PriorityQueue;

class GD 
{
    public static void main(String[] args) 
    {
        //PriorityQueue class implements the Queue interface
        PriorityQueue<String> pq=new PriorityQueue<>();
        pq.add("Apple");
        pq.add("Orange");
        pq.add("Mango");
        pq.add("Grapes");
        pq.add("Cherry");
        pq.add("Apple");
        pq.add("Blueberry");
        System.out.println(pq);
        System.out.println("Size: "+pq.size());
    }
}
