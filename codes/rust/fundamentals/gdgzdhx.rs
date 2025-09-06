// ----------------------------------------------------------------------------------------------------
// Title          : Rust program to accept the input from a user
// File Name      : gdgzdhx.rs
// Compiled       : rustc 1.84.1 (e71f9a9a9 2025-01-27) (built from a source tarball)
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

use std::io::{self, Write};
fn main()
{
    const PI:f32=3.14;
    let mut input=String::new();
    
    println!("———————————————————————————————————————————");
    println!("Program to calculate the area and circumference of a circle");
    println!("———————————————————————————————————————————");
    print!("Enter the radius of a circle ");
    io::stdout().flush().ok();
    io::stdin().read_line(&mut input).unwrap();
    let r:f32=input.trim().parse().unwrap();
    println!("The area of a circle is {a}",a=PI*r*r);
    println!("The circumference of a circle is {c}",c=2.0*PI*r);
    println!("———————————————————————————————————————————");
}
