// ----------------------------------------------------------------------------------------------------
// Title          : C# program to change the index of enum
// File Name      : gdbgvwn.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

Console.WriteLine("———————————————————————————————————————————");
Console.WriteLine("Program to change the index of enum");
Console.WriteLine("———————————————————————————————————————————");
foreach (CAccessories c in Enum.GetValues(typeof(CAccessories)))
{
    Console.WriteLine(c);
}
int i1 = (int)CAccessories.Speakers;
int i2 = (int)CAccessories.Skins;
Console.WriteLine("Speakers {0}", i1);
Console.WriteLine("Skins {0}", i2);
Console.WriteLine("———————————————————————————————————————————");

public enum CAccessories
{
    Keyboards, Mice, Speakers, Routers = 1000, Modems, CoolPads, UPS, Sleeves, Skins
};
