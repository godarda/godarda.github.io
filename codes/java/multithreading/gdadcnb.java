// ----------------------------------------------------------------------------------------------------
// Title          : Java program for a daemon thread
// File Name      : gdadcnb.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

class GD extends Thread
{  
    public void run()
    {  
        if(Thread.currentThread().isDaemon())
        {
            System.out.println("Daemon Thread Running");  
        }  
        else
        {  
            System.out.println("Thread Running");  
        }  
    }  
    public static void main(String args[])
    {  
        GD t1=new GD();
        GD t2=new GD();  
        t1.setDaemon(true);
        t1.start();
        t2.start();    
    }  
}
