// ----------------------------------------------------------------------------------------------------
// Title          : C# program to handle the TimeZoneNotFoundException
// File Name      : gdwxaed.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

var tz = TimeZoneInfo.ConvertTime(DateTime.Now, TimeZoneInfo.Local, TimeZoneInfo.FindSystemTimeZoneById("IndiaIndia Standard Time"));
Console.WriteLine(tz);
