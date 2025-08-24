// ----------------------------------------------------------------------------------------------------
// Title          : Java MySQL to update the table records
// File Name      : gdqkpvm.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

class GD
{
    public static void main(String[] args)
    {
        try
        {
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/DB","root", "godarda");
            Statement st = con.createStatement();
            st.executeUpdate("UPDATE holders SET amount = amount + 2000 WHERE account_no = 25622348993");
            System.out.println("List of all the records");
            ResultSet rs=st.executeQuery("SELECT * FROM holders");  
            while(rs.next())
            {
                System.out.println(rs.getLong("account_no")+", "+rs.getString("name")+", "+rs.getString("bank")+", "+rs.getDouble("amount"));
            }
            
            st.executeUpdate("UPDATE holders SET amount = amount + 2000");
            System.out.println("\nList of all the records");
            rs=st.executeQuery("SELECT * FROM holders");  
            while(rs.next())
            {
                System.out.println(rs.getLong("account_no")+", "+rs.getString("name")+", "+rs.getString("bank")+", "+rs.getDouble("amount"));
            }
            con.close();
        }
        catch(Exception e)
        {
            System.out.println(e.getMessage());
        }
    }
}
