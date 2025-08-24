// ----------------------------------------------------------------------------------------------------
// Title          : How to use TestNG Parameters and Data Provider for Data Driven Testing
// File Name      : gdekvaz.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

package tests;

import java.util.concurrent.TimeUnit;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.testng.annotations.Parameters;
import org.testng.annotations.Test;

public class VerifyTitle
{   
    WebDriver driver;
    
    @Test
    @Parameters("browser")
    public void OpenBrowser(String bname)
    {
        if(bname.equals("firefox"))
        {
            System.setProperty("webdriver.gecko.driver", "/home/godarda/drivers/geckodriver");
            driver = new FirefoxDriver();
        }
        else if (bname.equals("chrome")) 
        {
            System.setProperty("webdriver.chrome.driver", "/home/godarda/drivers/chromedriver");
            driver = new ChromeDriver();
        }
        else
        {
            System.out.println("Browser not found");
        }
        
        driver.navigate().to("http://newtours.demoaut.com");
        if(driver.getTitle().equals("Welcome: Mercury Tours"))
        {
            System.out.println("Test Passed");
        }
        else
        {
            System.out.println("Test Failed");
        }
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        driver.close();
    }
}
