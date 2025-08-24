// ----------------------------------------------------------------------------------------------------
// Title          : Implementation of Java LinkedHashMap class
// File Name      : gderzgx.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import java.util.LinkedHashMap;

class GD 
{
    public static void main(String[] args) 
    {
        //LinkedHashMap class implements the Map interface
        LinkedHashMap<Long,String> lhm = new LinkedHashMap<>();
        lhm.put(25622348989L,"James Moore");
        lhm.put(25622348990L,"Donald Taylor");
        lhm.put(25622348991L,"Edward Parkar");
        lhm.put(25622348992L,"Ryan Bakshi");
        System.out.println(lhm);
        System.out.println("Size: "+lhm.size());
    }
}
