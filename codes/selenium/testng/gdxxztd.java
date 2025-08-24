// ----------------------------------------------------------------------------------------------------
// Title          : How to run the same method multiple times using the invocationCount in TestNG
// File Name      : gdxxztd.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

package tests;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.Test;

public class KWTestNG 
{
    @Test(invocationCount = 3)
    public void NavigateLogin()
    {
        System.setProperty("webdriver.chrome.driver", "/home/godarda/drivers/chromedriver");
        WebDriver driver = new ChromeDriver();
        driver.manage().window().maximize();
        driver.navigate().to("http://newtours.demoaut.com");

        driver.findElement(By.name("userName")).sendKeys("mercury");
        driver.findElement(By.name("password")).sendKeys("mercury");
        driver.findElement(By.name("login")).click();
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
