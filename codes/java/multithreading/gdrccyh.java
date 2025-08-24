// ----------------------------------------------------------------------------------------------------
// Title          : Java program for Runnable interface
// File Name      : gdrccyh.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

class GD implements Runnable
{  
    public void run()
    {  
        System.out.println("Thread Running...");  
    }  
    public static void main(String args[])
    {  
        GD g=new GD();
        Thread t1=new Thread(g); 
        //t1.run();  
        System.out.println(t1.isAlive()); 
        t1.start(); 
        System.out.println(t1.isAlive());
    }  
}
