// ----------------------------------------------------------------------------------------------------
// Title          : How to get the size of heap in Java
// File Name      : gdzgzzw.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

class GD
{
    public static void main(String args[])
    {
        System.out.println("Max Heap Memory: "+Runtime.getRuntime().maxMemory());
        System.out.println("Total Heap Memory: "+Runtime.getRuntime().totalMemory());
        System.out.println("Free Heap Memory: "+Runtime.getRuntime().freeMemory());
    }
}
