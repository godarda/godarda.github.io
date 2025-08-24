// ----------------------------------------------------------------------------------------------------
// Title          : How to create multiline strings using Java text blocks
// File Name      : gdygaza.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

class GD 
{
    @SuppressWarnings("preview")
    public static void main(String[] args) 
    {
        String s1 = """
                Welcome
                to
                GoDarda""";
        String s2 = "Welcome\nto\nKodingWindow";
        System.out.println(s1);     //text block string
        System.out.println("———————————————————————");
        System.out.println(s2);     //normal string
        System.out.println("———————————————————————");
        System.out.println(s1==s2);
        System.out.println(s1.equals(s2));
    }
}
