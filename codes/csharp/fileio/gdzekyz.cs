// ----------------------------------------------------------------------------------------------------
// Title          : C# program to perform the operations on a file
// File Name      : gdzekyz.cs
// Compiled       : 8.0.119
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

try
{
    Console.WriteLine("———————————————————————————————————————————");
    Console.WriteLine("Program to perform the operations on a file");
    Console.WriteLine("———————————————————————————————————————————");
    FileStream f = new FileStream("/home/godarda/Trial.txt", FileMode.Append);
    //"Hi There!" text is present in Trial.txt
    StreamWriter w = new StreamWriter(f);
    w.WriteLine("Welcome to GoDarda!");
    w.Close();
    f.Close();

    FileStream fs = new FileStream("/home/godarda/Trial.txt", FileMode.Open);
    StreamReader r = new StreamReader(fs);
    string line = "";
    while ((line = r.ReadLine()) != null)
    {
        Console.WriteLine(line);
    }
    r.Close();
    fs.Close();
    Console.WriteLine("———————————————————————————————————————————");
}
catch (FileNotFoundException)
{
    Console.WriteLine("File not found");
}
catch (Exception e)
{
    Console.WriteLine(e);
}
finally
{
    Thread.Sleep(5000);
}
