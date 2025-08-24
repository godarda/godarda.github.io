// ----------------------------------------------------------------------------------------------------
// Title          : C# implementation of structure
// File Name      : gdchztk.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

Bank b1;
Bank b2;
b1.bank_name = "Barclays";
b1.holder_name = "Edward Parkar";
b1.balance = 19000;
b2.bank_name = "Citi";
b2.holder_name = "Donald Taylor";
b2.balance = 7000;
Console.WriteLine("———————————————————————————————————————————");
Console.WriteLine("Program to demonstrate the use of structure");
Console.WriteLine("———————————————————————————————————————————");
Console.WriteLine("Bank Name {0}", b1.bank_name);
Console.WriteLine("Holder Name {0}", b1.holder_name);
Console.WriteLine("Balance {0}", b1.balance);
Console.WriteLine("———————————————————————");
Console.WriteLine("Bank Name {0}", b2.bank_name);
Console.WriteLine("Holder Name {0}", b2.holder_name);
Console.WriteLine("Balance {0}", b2.balance);
Console.WriteLine("———————————————————————————————————————————");

struct Bank
{
    public string bank_name;
    public string holder_name;
    public double balance;
};
