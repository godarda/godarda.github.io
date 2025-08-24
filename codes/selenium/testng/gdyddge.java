// ----------------------------------------------------------------------------------------------------
// Title          : How to run parallel tests with Selenium WebDriver and TestNG
// File Name      : gdyddge.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

package tests;

import java.util.concurrent.TimeUnit;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.Test;

public class Login 
{
    @Test
    public void OpenChorme()
    {
        System.setProperty("webdriver.chrome.driver", "/home/godarda/drivers/chromedriver");
        System.out.println("Chrome Thread ID "+Thread.currentThread().getId());
        WebDriver driver = new ChromeDriver();
        driver.navigate().to("http://newtours.demoaut.com");
        driver.findElement(By.name("userName")).sendKeys("mercury");
        driver.findElement(By.name("password")).sendKeys("mercury");
        driver.findElement(By.name("login")).click();
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        driver.close();
    }
}
