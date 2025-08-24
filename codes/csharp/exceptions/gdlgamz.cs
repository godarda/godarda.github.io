// ----------------------------------------------------------------------------------------------------
// Title          : C# program to handle the PlatformNotSupportedException
// File Name      : gdlgamz.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

Thread t = Thread.CurrentThread;
t.Name = "Main Thread";
t.Abort();
