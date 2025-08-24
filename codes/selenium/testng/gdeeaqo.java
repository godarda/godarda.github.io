// ----------------------------------------------------------------------------------------------------
// Title          : How to use priority and dependencies in TestNG
// File Name      : gdeeaqo.java
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
    WebDriver driver;
    @Test(priority = 0)
    public void OpenBrowser()
    {
        System.out.println("Open Block");
        System.setProperty("webdriver.chrome.driver", "/home/godarda/drivers/chromedriver");
        driver = new ChromeDriver();
        driver.manage().window().maximize();
    }
    @Test(priority = 1)
    public void Navigate()
    {
        System.out.println("Navigation Block");
        driver.navigate().to("http://newtours.demoaut.com");
    }
    @Test(dependsOnMethods = {"Login"}, priority = 2)
    public void Logout()
    {
        System.out.println("Logout Block");
        driver.findElement(By.linkText("SIGN-OFF")).click();
        driver.close();
    }
    @Test(priority = 2)
    public void Login()
    {
        System.out.println("Login Block");
        driver.findElement(By.name("userName")).sendKeys("mercury");
        driver.findElement(By.name("password")).sendKeys("mercury");
        driver.findElement(By.name("login")).click();
    }
}
