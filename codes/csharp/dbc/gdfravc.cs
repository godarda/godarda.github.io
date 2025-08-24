// ----------------------------------------------------------------------------------------------------
// Title          : C# program to connect with MySQL Database
// File Name      : gdfravc.cs
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
            MySqlConnection con = new MySqlConnection("server=localhost;user=root;port=3306;password=passwd");
            try
            {
                con.Open();
                Console.WriteLine("Connection Established Successfully");
            }
            catch(Exception e)
            {
                Console.WriteLine(e.Message);
            }
            Console.ReadKey();
        }
    }
}
