// ----------------------------------------------------------------------------------------------------
// Title          : C# MySQL to insert and retrieve the records from a table
// File Name      : gdqzgqw.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

using MySql.Data.MySqlClient;
using System;
using System.Linq;
namespace GoDarda
{
    class Program
    {
        public static void Main(string[] args)
        {
            MySqlConnection con = new MySqlConnection("server=localhost;database=DB;user=root;port=3306;password=passwd;");
            MySqlCommand cmd;
            con.Open();
            cmd = new MySqlCommand("INSERT INTO holders(account_no,name,bank,amount) VALUES(@account_no,@name,@bank,@amount)", con);

            string[] lines = System.IO.File.ReadAllLines(@"D:/Data/gd.csv").Skip(1).ToArray();
            cmd.Parameters.Add(new MySqlParameter("@account_no", "account_no"));
            cmd.Parameters.Add(new MySqlParameter("@name", "name"));
            cmd.Parameters.Add(new MySqlParameter("@bank", "bank"));
            cmd.Parameters.Add(new MySqlParameter("@amount", "amount"));

            foreach (string line in lines)
            {
                string[] column = line.Split(',');
                cmd.Parameters["@account_no"].Value = column[0];
                cmd.Parameters["@name"].Value = column[1];
                cmd.Parameters["@bank"].Value = column[2];
                cmd.Parameters["@amount"].Value = column[3];
                cmd.Prepare();
                cmd.ExecuteNonQuery();
            }
            Console.WriteLine("Records inserted successfully");

            cmd = new MySqlCommand("SELECT * FROM holders", con);
            MySqlDataReader dr = cmd.ExecuteReader();
            Console.WriteLine("List of all the records");
            while (dr.Read())
            {
                Console.WriteLine(dr[0] + " " + dr[1] + " " + dr[2] + " " + dr[3]);
            }
            dr.Close();

            cmd = new MySqlCommand("SELECT * FROM holders WHERE amount >= 10000", con);
            dr = cmd.ExecuteReader();
            Console.WriteLine("\nList of the records after applying WHERE clause");
            while (dr.Read())
            {
                Console.WriteLine(dr[0] + " " + dr[1] + " " + dr[2] + " " + dr[3]);
            }
            dr.Close();
            con.Close();

            Console.ReadKey();
        }
    }
}
