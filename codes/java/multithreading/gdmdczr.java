// ----------------------------------------------------------------------------------------------------
// Title          : Java program for getName(), getId() and getPriority() methods
// File Name      : gdmdczr.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

class GD
{
    public static void main(String[] args)
    {
        Thread t1=Thread.currentThread();
        System.out.println("Thread Name "+t1.getName());
        System.out.println("Thread Priority "+t1.getPriority());
        t1.setName("My Thread");
        System.out.println("Name "+t1);
    }
}
