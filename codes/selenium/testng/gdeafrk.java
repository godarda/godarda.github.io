// ----------------------------------------------------------------------------------------------------
// Title          : How to define dependencies between groups in TestNG XML file
// File Name      : gdeafrk.java
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
    @Test(groups = {"OpenBrowserNavigate"})
    public void OpenBrowserNavigate()
    {
        System.setProperty("webdriver.chrome.driver", "/home/godarda/drivers/chromedriver");
        driver = new ChromeDriver();
        driver.manage().window().maximize();
        driver.navigate().to("http://newtours.demoaut.com");
    }
    @Test(groups = {"LoginLogout"})
    public void LoginLogout()
    {
        driver.findElement(By.name("userName")).sendKeys("mercury");
        driver.findElement(By.name("password")).sendKeys("mercury");
        driver.findElement(By.name("login")).click();
        driver.findElement(By.linkText("SIGN-OFF")).click();
        driver.close();
    }
}
