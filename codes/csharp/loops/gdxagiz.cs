// ----------------------------------------------------------------------------------------------------
// Title          : C# program to use the loops and control statements
// File Name      : gdxagiz.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

Console.WriteLine("———————————————————————————————————————————");
Console.WriteLine("Program to use the control statements");
Console.WriteLine("———————————————————————————————————————————");
int i = 0;
do
{
    i++;
    if (i == 9)
    {
        break;
    }
    if(i == 6)
    {
        continue;
    }
    Console.WriteLine(i); 
} while(i <= 10);
goto Execute;
Execute:
Console.WriteLine("Executed goto statement");
Console.WriteLine("———————————————————————————————————————————");
