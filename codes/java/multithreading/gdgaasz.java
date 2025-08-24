// ----------------------------------------------------------------------------------------------------
// Title          : Java program to extends the Thread class
// File Name      : gdgaasz.java
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
        GD g=new GD();  
        g.start();  
    }  
}
