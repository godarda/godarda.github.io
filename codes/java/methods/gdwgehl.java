// ----------------------------------------------------------------------------------------------------
// Title          : Java program to format the text blocks strings using formatted() method
// File Name      : gdwgehl.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

class GD 
{
    @SuppressWarnings({ "preview", "removal" })
    public static void main(String[] args) 
    {
        String s1 = """
                account_no: %d
                name: %s
                city: %s
                amount: %.2f
                """.formatted(25622348989L,"James Moore","Phoenix",5000.002335);
        System.out.println(s1);
    }
}
