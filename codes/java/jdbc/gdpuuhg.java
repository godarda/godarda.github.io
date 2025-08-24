// ----------------------------------------------------------------------------------------------------
// Title          : Java MySQL to connect, create database, and table
// File Name      : gdpuuhg.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

class GD
{
    public static void main(String[] args) 
    {
        String dbname="DB";
        try
        {
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306","root", "godarda");
            System.out.println("Connection Established Successfully");
            Statement st = con.createStatement();
            st.executeUpdate("DROP DATABASE IF EXISTS "+ dbname + "");
            st.executeUpdate("CREATE DATABASE "+ dbname + "");
            System.out.println("Database Created");
            
            con.close();
            System.out.println("Connection Released Successfully");
        }
        catch(Exception e)
        {
            System.out.println(e.getMessage());
        }
    }
}
