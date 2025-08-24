// ----------------------------------------------------------------------------------------------------
// Title          : Java program to perform multiple tasks by multiple threads
// File Name      : gdaedsw.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

class task1 extends Thread
{
    public void run()
    {  
        System.out.println("\nTask-1");  
    }
    public void inc()
    {
        for(int i=100;i<=105;i++)
        {
            System.out.print(i+" ");     
        }  
    } 
}
class task2 extends Thread
{
    public void run()
    {  
        System.out.println("\nTask-2");  
    } 
}

class GD 
{  
    public static void main(String args[])
    {  
        task1 t1=new task1();
        task2 t2=new task2(); 
        t1.inc();
        t1.start();
        t2.start(); 
    }  
}
