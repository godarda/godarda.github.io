// ----------------------------------------------------------------------------------------------------
// Title          : F# program to check the given number is even or odd
// File Name      : gdzegce.fs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

open System

Console.Write("Enter the number ")
let n = int32(Console.ReadLine())
if(n >= 0) then 
    printfn "%i is an EVEN number" n
else 
    printfn "%i is an ODD number" n
