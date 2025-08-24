// ----------------------------------------------------------------------------------------------------
// Title          : Java MySQL to perform JDBC CRUD operations
// File Name      : gdbylyk.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.InputMismatchException;
import java.util.Random;
import java.util.Scanner;

public class Employee
{
    static String empid;
    static int ch;
    static String fname="";
    static String lname="";
    static String mob="";
    static String designation="";
    static double salary=0;
    static String city="";
    static Scanner sc = new Scanner(System.in);
    static DataStoreHelper dsh = new DataStoreHelper();
    
    public Employee(String empid, String fname, String lname, String mob, String designation, double salary, String city)
    {
        Employee.empid=empid;
        Employee.fname=fname;
        Employee.lname=lname;
        Employee.mob=mob;
        Employee.designation=designation;
        Employee.salary=salary;
        Employee.city=city;
    }
    
    public static String empid()
    {
        String alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String digits = "0123456789";
        Random r = new Random();
        String genrate = "";
        while (genrate.length () != 7)
        {
            int rPick = r.nextInt(4);
            if (rPick == 1)
            {
                genrate += alphabets.charAt(r.nextInt(25));
            }
            else if (rPick == 3)
            {
                genrate += digits.charAt(r.nextInt(9));
            }
        }
        empid="KW_"+genrate;
        System.out.println("\nGenerated Employee ID " + empid);
        return empid;
    }
    
    static String mobile()
    {
        System.out.print("\nEnter Mobile Number ");
        mob=sc.next();
        if(mob.matches("\\d{10}"))
        {
            System.out.println("Mobile Number is Accepted");
        }
        else
        {
            System.out.println("Mobile Number is Not Valid (Must be 10 Digit)");
            mobile();
        }
        return mob;
    }
    
    static String select_desig()
    {
        do
        {
            try
            {
                System.out.println("________________________________");
                System.out.println("Select Your Designation");
                System.out.println("________________________________");
                System.out.println("1. Software Engineer\n2. Consultant\n3. Manager\n4. Other");
                System.out.println("________________________________");
                System.out.print("Enter Your Choice ");
                ch = sc.nextInt();
            }
            catch(InputMismatchException ime)
            {
                System.out.println("\nWrong Choice Entered... Please Try Again");
                select_desig();
            }
            switch(ch)
            {
                case 1:
                    designation="Software Engineer";
                    salary=20000;
                    break;
                case 2:
                    designation="Consultant";
                    salary=25000;
                    break;
                case 3:
                    designation="Manager";
                    salary=30000;
                    break;
                case 4:
                    designation="Other";
                    salary=15000;
                    break;
                default:
                    System.out.println("\nWrong Choice Entered... Please Try Again");
            }
            
        } while (ch!=1&ch!=2&ch!=3&ch!=4);
        return designation;
    }
    
    static String city()
    {
        String regex = "^[a-zA-Z]+$";
        System.out.print("\nEnter Your City ");
        city=sc.next();
        if(city.matches(regex)&&city.length()>=3)
        {
            System.out.println("City Name is Accepted");
        }
        else
        {
            System.out.println("Invalid City \n(Contains only alphabets and length should be greater than 2)");
            city();
        }
        return city;
    }
    
    static String firstname()
    {
        String regex = "^[a-zA-Z]+$";
        System.out.print("\nEnter First Name ");
        fname=sc.next();
        
        if(fname.matches(regex)&&fname.length()>=2)
        {
            System.out.println("FirstName is Accepted");
        }
        else
        {
            System.out.println("Invalid FirstName \n(Contains only alphabets and length should be greater than 2)");
            firstname();
        }
        return fname;
    }
    
    static String lastname()
    {
        String regex = "^[a-zA-Z]+$";
        System.out.print("\nEnter Last Name ");
        lname=sc.next();
        
        if(lname.matches(regex)&&lname.length()>=2)
        {
            System.out.println("LastName is Accepted");
        }
        else
        {
            System.out.println("Invalid LastName \n(Contains only alphabets and length should be greater than 2)");
            firstname();
        }
        return lname;
    }
    
    public static void mainMenu() throws ClassNotFoundException, SQLException, IOException
    {
        do
        {
            try
            {
                System.out.println("________________________________");
                System.out.println("Welcome to GoDarda Portal");
                System.out.println("________________________________");
                System.out.println("1. Admin Login\n2. Sign In\n3. Sign Up\n4. Exit");
                System.out.println("________________________________");
                System.out.print("Enter Your Choice ");
                ch = sc.nextInt();
            }
            catch(InputMismatchException ime)
            {
                System.out.println("\nWrong Choice Entered... Please Try Again");
                mainMenu();
            }
            
            switch(ch)
            {
                case 1:
                    System.out.print("\nEnter User Name ");
                    String uname=sc.next();
                    System.out.print("\nEnter Password ");
                    String password=sc.next();
                    
                    if(uname.equalsIgnoreCase("admin")&&password.equalsIgnoreCase("admin"))
                    {
                        do
                        {
                            System.out.println("________________________________");
                            System.out.println("1. Display All Employees\n2. Update Info\n3. Delete All Account\n4. Go to MainMenu");
                            System.out.println("________________________________");
                            System.out.print("Enter Your Choice ");
                            try
                            {
                                ch = sc.nextInt();
                            }
                            catch(InputMismatchException ime)
                            {
                                System.out.println("\nWrong Choice Entered... Please Try Again");
                            }
                            switch(ch)
                            {
                                case 1:
                                    try
                                    {
                                        dsh.viewAllEmployee(empid);
                                    }
                                    catch(Exception e)
                                    {
                                        System.out.println(e);
                                    }
                                    break;
                                case 2:
                                    break;
                                case 3:
                                    try
                                    {
                                        dsh.dropAllEmployee();
                                    }
                                    catch(Exception e)
                                    {
                                        System.out.println(e);
                                    }
                                    break;
                                case 4:
                                    mainMenu();
                                default:
                                    System.out.println("\nWrong Choice Entered... Please Try Again");
                            }
                        } while (ch!=4);
                        
                    }
                    else
                    {
                        System.out.println("\nWrong Username and Password");
                        mainMenu();
                    }
                    break;
                case 2:
                    System.out.print("\nEnter Employee ID ");
                    String emp=sc.next();
                    
                    if(emp.equals(empid))
                    {
                        do
                        {
                            System.out.println("________________________________");
                            System.out.println("1. Display Info\n2. Update Info\n3. Remove Account\n4. Go to MainMenu");
                            System.out.println("________________________________");
                            System.out.print("Enter Your Choice ");
                            try
                            {
                                ch = sc.nextInt();
                            }
                            catch(InputMismatchException ime)
                            {
                                System.out.println("\nWrong Choice Entered... Please Try Again");
                            }
                            switch(ch)
                            {
                                case 1:
                                    try
                                    {
                                        dsh.viewEmployee(empid);
                                    }
                                    catch(Exception e)
                                    {
                                        System.out.println(e);
                                    }
                                    break;
                                case 2:
                                    dsh.updateEmployee(empid);
                                    break;
                                case 3:
                                    dsh.removeEmployee(empid);
                                    break;
                                case 4:
                                    mainMenu();
                                default:
                                    System.out.println("\nWrong Choice Entered... Please Try Again");
                            }
                        } while (ch!=4);
                    }
                    else
                    {
                        mainMenu();
                    }
                    System.out.println(empid);
                    break;
                case 3:
                    empid();
                    
                    firstname();
                    
                    lastname();
                    
                    mobile();
                    
                    select_desig();
                    
                    city();
                    
                    Employee e = new Employee(empid,fname,lname,mob,designation,salary,city);
                    try
                    {
                        dsh.addEmployee(e);
                    }
                    catch(Exception ex)
                    {
                        System.out.println(ex);
                    }
                    
                    break;
                case 4:
                    System.exit(0);
                default:
                    System.out.println("\nWrong Choice Entered... Please Try Again");
            }
        } while (ch!=4);
    }

    public static void main(String[] args) throws ClassNotFoundException, IOException, SQLException
    {
        try
        {
            Class.forName("com.mysql.cj.jdbk.Driver");
        }
        catch (ClassNotFoundException e)
        {
            System.out.println("Please load MySQL JDBC driver");
            e.printStackTrace();
            return;
        }
        Connection con;
        try
        {
            con = DriverManager.getConnection("jdbc:mysql://localhost:3306/data","root", "godarda");
            System.out.println("Connection Established");
            
        }
        catch (SQLException e)
        {
            System.out.println("Connection Failed");
            e.printStackTrace();
            return;
        }
        
        Statement st=con.createStatement();
        //st.executeUpdate("DROP TABLE EMPLOYEES");
        st.executeUpdate("CREATE TABLE EMPLOYEES(EMPID VARCHAR(11) PRIMARY KEY,FNAME VARCHAR(20),LNAME VARCHAR(20),MOB INT(10),DESIGNATION VARCHAR(20), SALARY INT(20), CITY VARCHAR(15))");
        System.out.println("Employees Table Created Successfully");
        mainMenu();
    }
    
}
