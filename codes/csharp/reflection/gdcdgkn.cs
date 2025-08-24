// ----------------------------------------------------------------------------------------------------
// Title          : C# program to demonstrate the use of reflection objects
// File Name      : gdcdgkn.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

Console.WriteLine("———————————————————————————————————————————");
Console.WriteLine("Program to use Reflection objects");
Console.WriteLine("———————————————————————————————————————————");
int i = 0;
float f = 0.0F;
Type t1 = i.GetType();
Type t2 = f.GetType();
Type t3 = typeof(System.String);
Console.WriteLine(t1);
Console.WriteLine(t2);
Console.WriteLine(t3.Assembly);
Console.WriteLine(t3.FullName);
Console.WriteLine(t3.BaseType);
Console.WriteLine(t3.IsClass);
Console.WriteLine(t3.IsEnum);
Console.WriteLine(t3.IsInterface);  
Console.WriteLine("———————————————————————————————————————————");
