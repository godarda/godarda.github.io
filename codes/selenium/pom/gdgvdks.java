// ----------------------------------------------------------------------------------------------------
// Title          : Selenium Java Page Object Model with Page Factory
// File Name      : gdgvdks.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

package tests;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;

public class BasePOM 
{
    public static WebDriver driver=null;
    @BeforeClass
    public void OpenBrowser()
    {
        System.setProperty("webdriver.chrome.driver", "/home/godarda/drivers/chromedriver");
        driver = new ChromeDriver();
        driver.manage().window().maximize();
        driver.navigate().to("http://newtours.demoaut.com");
    }
    @AfterClass
    public void CloseBrowser()
    {
        driver.close();
    }
}
