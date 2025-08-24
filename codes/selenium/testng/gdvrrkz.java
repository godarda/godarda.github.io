// ----------------------------------------------------------------------------------------------------
// Title          : How to use TestNG Annotations in Selenium
// File Name      : gdvrrkz.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

package tests;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterClass;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.BeforeMethod;

public class BaseAnnotations 
{
    WebDriver driver;
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
    @BeforeMethod
    public void Login()
    {
        driver.findElement(By.name("userName")).sendKeys("mercury");
        driver.findElement(By.name("password")).sendKeys("mercury");
        driver.findElement(By.name("login")).click();
    }
    @AfterMethod
    public void Logout() 
    {
        driver.findElement(By.linkText("SIGN-OFF")).click();
    }
}
