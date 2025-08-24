// ----------------------------------------------------------------------------------------------------
// Title          : C# program for sleep(), abort() and join() methods
// File Name      : gdqikyq.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

Thread t1 = new Thread(new ThreadStart(KWThread.thread));
Thread t2 = new Thread(new ThreadStart(KWThread.thread));
t1.Start();
t2.Start();
t1.Join();
Console.WriteLine("Thread Interrupted");
t1.Interrupt();
t2.Interrupt();

public class KWThread
{
    public static void thread()
    {
        for (int i = 0; i < 5; i++)
        {
            Console.Write(i + " ");
            Thread.Sleep(200);
        }
    }
}
