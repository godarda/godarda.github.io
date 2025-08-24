// ----------------------------------------------------------------------------------------------------
// Title          : C# program to create a database in MySQL
// File Name      : gdraazt.cs
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
            string dbname = "DB";
            MySqlConnection con = new MySqlConnection("server=localhost;user=root;port=3306;password=passwd");
            MySqlCommand cmd;
            try
            {
                con.Open();
                Console.WriteLine("Connection Established Successfully");
                cmd = new MySqlCommand("DROP DATABASE IF EXISTS " + dbname + "", con);
                cmd.ExecuteNonQuery();

                cmd = new MySqlCommand("CREATE DATABASE "+ dbname + "", con);
                cmd.ExecuteNonQuery();
                Console.WriteLine("Database Created");
                
                Console.WriteLine("\nList of MySQL Databases: ");
                cmd = new MySqlCommand("SHOW DATABASES", con);
                MySqlDataReader dr = cmd.ExecuteReader();
                while (dr.Read())
                {
                    Console.WriteLine(dr[0]);
                }
                dr.Close();
                con.Close();
                Console.WriteLine("\nConnection Released Successfully");
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
            Console.ReadKey();
        }
    }
}
