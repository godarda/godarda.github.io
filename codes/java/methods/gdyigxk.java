// ----------------------------------------------------------------------------------------------------
// Title          : Java program to get the Operating System details
// File Name      : gdyigxk.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

class GD
{
    public static void main(String args[])
    {
        System.out.println("OS Name: "+System.getProperty("os.name"));
        System.out.println("OS Version: "+System.getProperty("os.version"));
        System.out.println("OS Architecture: "+System.getProperty("os.arch"));
        
        System.out.println("Java Version: "+System.getProperty("java.version"));
        System.out.println("Java Vendor URL: "+System.getProperty("java.vendor.url")); 
    }
}
