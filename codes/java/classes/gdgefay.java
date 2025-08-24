// ----------------------------------------------------------------------------------------------------
// Title          : Java implementation of Calendar class
// File Name      : gdgefay.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import java.util.Calendar;
class GD
{
    public static void main(String args[])
    {
        Calendar c=Calendar.getInstance();
        System.out.println("———————————————————————————————————————————");
        System.out.println("Java implementation of Calendar class");
        System.out.println("———————————————————————————————————————————");
        System.out.println("Year          | "+c.get(Calendar.YEAR));
        System.out.println("Month         | "+c.get(Calendar.MONTH));
        System.out.println("Day of Month  | "+c.get(Calendar.DAY_OF_MONTH));
        System.out.println("Day of Week   | "+c.get(Calendar.DAY_OF_WEEK)); 
        System.out.println("Week of Month | "+c.get(Calendar.WEEK_OF_MONTH));
        System.out.println("DOW in Month  | "+c.get(Calendar.DAY_OF_WEEK_IN_MONTH));
        System.out.println("Hour          | "+c.get(Calendar.HOUR));
        System.out.println("Minute        | "+c.get(Calendar.MINUTE));
        System.out.println("Seconds       | "+c.get(Calendar.SECOND));
        System.out.println("Time AM-0/PM-1| "+c.get(Calendar.AM_PM));
        System.out.println("———————————————————————————————————————————");
    }
}
