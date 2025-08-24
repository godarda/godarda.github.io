// ----------------------------------------------------------------------------------------------------
// Title          : C# program to demonstrate two threads working concurrently
// File Name      : gdziyve.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

Thread t1 = new Thread(new ThreadStart(ParallelThread.thread1));
Thread t2 = new Thread(new ThreadStart(ParallelThread.thread2));

t1.Start();
t2.Start();

class ParallelThread
{
    public static void thread1()
    {
        for (int i = 100; i <= 105; i++)
        {
            Console.Write(i + " ");
            Thread.Sleep(1500);
        }
    }
    public static void thread2()
    {
        for (int i = 200; i <= 205; i++)
        {
            Console.Write(i + " ");
            Thread.Sleep(1000);
        }
    }
}
