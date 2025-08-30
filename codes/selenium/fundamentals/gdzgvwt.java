// ----------------------------------------------------------------------------------------------------
// Title          : Selenium Java to compare the title of a given webpage
// File Name      : gdzgvwt.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

class GD 
{
    public static void main(String[] args) 
    {
        System.setProperty("webdriver.chrome.driver", "/home/godarda/drivers/chromedriver");
        WebDriver driver = new ChromeDriver();
        driver.navigate().to("https://godarda.in/testapp/");

        String actualTitle = driver.getTitle();
        String expectedTitle = "GoDarda's Testapp";

        System.out.println("Actual Title - "+actualTitle);
        System.out.println("Expected Title - "+expectedTitle);
        
        if(actualTitle.contentEquals(expectedTitle))
        {
            System.out.println("Title Matched");
        }
        else
        {
            System.out.println("Title Not Matched");
        }
        driver.close();
    }
}
