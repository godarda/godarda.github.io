// ----------------------------------------------------------------------------------------------------
// Title          : Selenium Java to get the current date and time using sendKeys
// File Name      : gdlwmed.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

class GD
{
    public static void main(String[] args) 
    {   
        System.setProperty("webdriver.chrome.driver", "/home/godarda/drivers/chromedriver");
        WebDriver driver = new ChromeDriver();
        
        driver.get("https://www.google.co.in/");
        driver.findElement(By.tagName("textarea")).sendKeys("Current Time In India");
        driver.findElement(By.tagName("textarea")).sendKeys(Keys.ENTER);
    }
}
