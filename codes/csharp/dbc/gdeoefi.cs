// ----------------------------------------------------------------------------------------------------
// Title          : C# program to create a table in MySQL
// File Name      : gdeoefi.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

using MySql.Data.MySqlClient;
using System;
namespace GoDarda
{
    class Program
    {
        public static void Main(string[] args)
        {
            MySqlConnection con = new MySqlConnection("server=localhost;database=DB;user=root;port=3306;password=passwd");
            MySqlCommand cmd;
            try
            {
                con.Open();
                cmd = new MySqlCommand("CREATE TABLE holders(account_no BIGINT PRIMARY KEY, name VARCHAR(30) NOT NULL, bank VARCHAR(10), amount BIGINT NOT NULL)", con);
                cmd.ExecuteNonQuery();
                Console.WriteLine("Table Created");
                
                Console.WriteLine("\nList of MySQL Tables: ");
                cmd = new MySqlCommand("SHOW TABLES", con);
                MySqlDataReader dr = cmd.ExecuteReader();
                while (dr.Read())
                {
                    Console.WriteLine(dr[0]);
                }
                dr.Close();
                con.Close();
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
            Console.ReadKey();
        }
    }
}
