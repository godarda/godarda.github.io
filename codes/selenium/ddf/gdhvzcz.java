// ----------------------------------------------------------------------------------------------------
// Title          : How to read an Excel file using Apache POI
// File Name      : gdhvzcz.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

public class ReadExcel 
{
    public static void main(String[] args)
    {
        try 
        {
            FileInputStream fis = new FileInputStream(new File("D://Selenium//Workbook-1.xlsx"));
            XSSFWorkbook workbook = new XSSFWorkbook(fis);
            XSSFSheet sheet = workbook.getSheetAt(0);
            int rowcnt = sheet.getLastRowNum();
            for(int i=0;i<=rowcnt;i++) 
            {
                Row r = sheet.getRow(i);
                for(int j=0;j<r.getLastCellNum();j++)
                {
                    System.out.print(r.getCell(j).toString()+" ");
                }
                System.out.println();
            }
            
            System.out.println("Number of Columns: "+sheet.getRow(0).getLastCellNum());
            System.out.println("Number of Rows: "+sheet.getLastRowNum());
        } 
        catch (IOException e) 
        {
            e.printStackTrace();
        }
    }
}
