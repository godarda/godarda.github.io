// ----------------------------------------------------------------------------------------------------
// Title          : C# program to implement Thread class and its properties
// File Name      : gdvkyzy.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

Thread t = Thread.CurrentThread;
t.Name = "Main Thread";
Console.WriteLine(t.Name);
Console.WriteLine(t.Priority);
Console.WriteLine(t.IsAlive);
Console.WriteLine(t.CurrentCulture);
Console.WriteLine(t.IsThreadPoolThread);
Console.WriteLine(t.ManagedThreadId);
Console.WriteLine(t.ThreadState);
