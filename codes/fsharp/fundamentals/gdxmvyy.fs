// ----------------------------------------------------------------------------------------------------
// Title          : F# program to calculate the area and circumference of a circle
// File Name      : gdxmvyy.fs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

open System

printfn "———————————————————————————————————————————"
printfn "Program to calculate the area and circumference of a circle"
printfn "———————————————————————————————————————————"
printf "Enter the radius of a circle "
let r = float(Console.ReadLine())
printfn "The area of a circle is %f " (Math.PI * r * r)
printfn "The circumference of a circle is %f " (float(2) * Math.PI * r)
printfn "———————————————————————————————————————————"
