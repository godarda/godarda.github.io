// ----------------------------------------------------------------------------------------------------
// Title          : C# implementation of Multithreading
// File Name      : gdaycye.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

Console.WriteLine("———————————————————————————————————————————");
Thread t = Thread.CurrentThread;
t.Name = "Main Thread";
Console.WriteLine(t.Name);

KWThread1 kwt1 = new KWThread1();
Thread A = new Thread(new ThreadStart(kwt1.thread));
Thread B = new Thread(new ThreadStart(kwt1.thread));
A.Start();
B.Start();

KWThread2 kwt2 = new KWThread2();
Thread C = new Thread(new ThreadStart(kwt2.thread));
Thread D = new Thread(new ThreadStart(kwt2.thread));
C.Start();
D.Start();
Console.WriteLine("\n———————————————————————————————————————————");

class KWThread1
{
    public void thread()
    {
        for (int i = 100; i < 105; i++)
        {
            Console.Write(i + " ");
        }
    }
}

class KWThread2
{
    public void thread()
    {
        for (int i = 0; i < 5; i++)
        {
            Console.Write(i + " ");
        }
        Console.WriteLine();
    }
}
