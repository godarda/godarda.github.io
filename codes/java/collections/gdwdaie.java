// ----------------------------------------------------------------------------------------------------
// Title          : Implementation of Java Stack class
// File Name      : gdwdaie.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import java.util.Stack;

class GD 
{
    public static void main(String[] args) 
    {
        Stack<String> s=new Stack<>();
        s.push("Apple");
        s.push("Orange");
        s.push("Mango");
        s.push("Grapes");
        s.push("Cherry");
        s.push("Apple");
        s.push("Blueberry");
        
        while(s.empty()==false)
        {
            System.out.println(s.pop());
        }
        
        /*
         * for(String e:s) { System.out.println(e); }
         */
    }
}
