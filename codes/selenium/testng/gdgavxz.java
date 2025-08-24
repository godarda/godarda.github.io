// ----------------------------------------------------------------------------------------------------
// Title          : How to use and implement TestNG Listeners
// File Name      : gdgavxz.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

package tests;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.Listeners;
import org.testng.annotations.Test;

@Listeners(tests.KWListener.class)  
public class KWTestNG 
{
    WebDriver driver;
    
    @Test(priority = 0)
    public void OpenBrowser()
    {
        System.setProperty("webdriver.chrome.driver", "/home/godarda/drivers/chromedriver");
        driver = new ChromeDriver();
        driver.manage().window().maximize();
        driver.navigate().to("http://newtours.demoaut.com");
    }
    @Test(priority = 1)
    public void Login()
    {
        driver.findElement(By.name("userName")).sendKeys("mercury");
        driver.findElement(By.name("password")).sendKeys("mercury");
        driver.findElement(By.name("login")).click();
    }
    @Test(priority = 2)
    public void VerifyTitle()
    {
        if(driver.getTitle().equals("Find a Flight: Mercury Tours:"))
        {
            System.out.println("Login Successful");
        }
        else
        {
            System.out.println("Login Unsuccessful");
        }
        driver.close();
    }
}
