// ----------------------------------------------------------------------------------------------------
// Title          : Java MySQL to insert and retrieve the records from a table
// File Name      : gdyszqa.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import java.io.FileReader;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

import com.opencsv.CSVReader;
import com.opencsv.CSVReaderBuilder;

class GD
{
    public static void main(String[] args)
    {
        try
        {
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/DB","root", "godarda");
            PreparedStatement statement = con.prepareStatement("INSERT INTO holders(account_no,name,bank,amount) VALUES(?,?,?,?)");
                    
            CSVReader reader = new CSVReaderBuilder(new FileReader("gd.csv")).withSkipLines(1).build();
            String[] column;
            while((column = reader.readNext()) != null) 
            {
                String account_no=column[0];
                String name=column[1];
                String bank=column[2];
                String amount=column[3];
                
                statement.setString(1,account_no);
                statement.setString(2,name);
                statement.setString(3,bank);
                statement.setString(4,amount);
                statement.addBatch();
            }
            statement.executeBatch();
            System.out.println("Records inserted successfully");
            
            System.out.println("List of all the records");
            ResultSet rs=statement.executeQuery("SELECT * FROM holders");  
            while(rs.next())
            {
                System.out.println(rs.getLong("account_no")+", "+rs.getString("name")+", "+rs.getString("bank")+", "+rs.getDouble("amount"));
            }
            
            System.out.println("\nList of the records after applying WHERE clause");
            rs=statement.executeQuery("SELECT * FROM holders WHERE amount >= 10000");  
            while(rs.next())
            {
                System.out.println(rs.getLong("account_no")+", "+rs.getString("name")+", "+rs.getString("bank")+", "+rs.getDouble("amount"));
            }
        }
        catch(Exception e)
        {
            System.out.println(e.getMessage());
        }
    }
}
