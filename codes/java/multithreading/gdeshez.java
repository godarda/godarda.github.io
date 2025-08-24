// ----------------------------------------------------------------------------------------------------
// Title          : Java program for join() and sleep() methods
// File Name      : gdeshez.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

class GD extends Thread
{  
    public void run()
    {  
        for(int i=100;i<=105;i++)
        {
            try
            {  
                Thread.sleep(500);  
            }
            catch(Exception e)
            {
                System.out.println(e);
            } 
            System.out.print(i+" ");     
        }  
        System.out.println("\n———————————————————————————————————————————");
    }  
    public static void main(String args[])
    {  
        System.out.println("———————————————————————————————————————————");
        System.out.println("Implementation of Java multithreading");
        System.out.println("———————————————————————————————————————————");
        GD t1=new GD();
        GD t2=new GD(); 
        t1.start();
        try
        {  
            t1.join(500);  
        }
        catch(Exception e)
        {
            System.out.println(e);
        }
        t2.start();
    }  
}
