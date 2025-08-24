// ----------------------------------------------------------------------------------------------------
// Title          : F# program to check the given number is positive or negative
// File Name      : gdhadwu.fs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

open System

Console.Write("Enter the number ")
let n = int32(Console.ReadLine())

if n < 0 then printfn "%i is a negative number" n
elif n > 0 then printfn "%i is a positive number" n
else printfn "Given number is Zero"
