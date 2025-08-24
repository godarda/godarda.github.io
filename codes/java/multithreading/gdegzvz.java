// ----------------------------------------------------------------------------------------------------
// Title          : Java program for priority thread
// File Name      : gdegzvz.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

class GD extends Thread
{  
    public void run()
    {  
        System.out.println(Thread.currentThread().getName()+" Server Is Running...");       
    }  
    public static void main(String args[])
    {  
        GD t1=new GD();
        GD t2=new GD(); 
        GD t3=new GD(); 
        t1.setName("MongoDB");
        t2.setName("MySQL");
        t3.setName("Cassandra");
        t1.setPriority(Thread.MAX_PRIORITY);
        t2.setPriority(Thread.NORM_PRIORITY);
        t3.setPriority(Thread.MIN_PRIORITY);
        System.out.println("Thread Priority T1 "+t1.getPriority());
        System.out.println("Thread Priority T2 "+t2.getPriority());
        System.out.println("Thread Priority T3 "+t3.getPriority());
        t1.start(); 
        t2.start();
        t3.start();  
    }  
}
