// ----------------------------------------------------------------------------------------------------
// Title          : Java program to perform a single task by multiple threads
// File Name      : gdyiztd.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

class GD extends Thread
{  
    public void run()
    {  
        System.out.println("Thread Running...");  
    }  
    public static void main(String args[])
    {  
        GD t1=new GD();
        GD t2=new GD(); 
        t1.start();
        t2.start(); 
    }  
}
