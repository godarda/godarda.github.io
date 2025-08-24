// ----------------------------------------------------------------------------------------------------
// Title          : Implementation of Java HashMap class
// File Name      : gdeydav.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import java.util.HashMap;

class GD 
{
    public static void main(String[] args) 
    {
        //HashMap class implements the Map interface
        HashMap<Long,String> hm = new HashMap<>();
        hm.put(25622348989L,"James Moore");
        hm.put(25622348990L,"Donald Taylor");
        hm.put(25622348991L,"Edward Parkar");
        hm.put(25622348992L,"Ryan Bakshi");
        System.out.println(hm);
        System.out.println("Size: "+hm.size());
    }
}
