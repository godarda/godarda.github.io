// ----------------------------------------------------------------------------------------------------
// Title          : C# program to achieve thread synchronization using the lock keyword
// File Name      : gdvyzkd.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

ParallelThread pt = new ParallelThread();
Thread t1 = new Thread(new ThreadStart(pt.thread));
Thread t2 = new Thread(new ThreadStart(pt.thread));

t1.Start();
t2.Start();

class ParallelThread
{
    public void thread()
    {
        lock (this)
        {
            for (int i = 100; i <= 105; i++)
            {
                Console.Write(i + " ");
                Thread.Sleep(1500);
            }
        }
    }
}
