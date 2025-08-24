// ----------------------------------------------------------------------------------------------------
// Title          : C# program to set the priorities to the threads
// File Name      : gdzfcze.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

PriorityThread pt = new PriorityThread();
Thread t1 = new Thread(new ThreadStart(pt.thread));
Thread t2 = new Thread(new ThreadStart(pt.thread));
Thread t3 = new Thread(new ThreadStart(pt.thread));
t1.Name = "MongoDB";
t2.Name = "Cassendra";
t3.Name = "MySQL";
t2.Priority = ThreadPriority.Highest;
t3.Priority = ThreadPriority.Normal;
t1.Priority = ThreadPriority.Lowest;
t1.Start();
t2.Start();
t3.Start();

public class PriorityThread
{
    public void thread()
    {
        Thread t = Thread.CurrentThread;
        Console.WriteLine(t.Name + " Server Is Running");
    }
}
