// ----------------------------------------------------------------------------------------------------
// Title          : Selenium Java to get the tag name
// File Name      : gdavegp.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

class GD 
{
    public static void main(String[] args) 
    {
        System.setProperty("webdriver.chrome.driver", "/home/godarda/drivers/chromedriver");
        WebDriver driver = new ChromeDriver();

        driver.get("https://godarda.github.io/testapp/");
        System.out.println(driver.findElement(By.name("username")).getTagName());
        System.out.println(driver.findElement(By.name("password")).getTagName());
        System.out.println(driver.findElement(By.name("login")).getTagName());
        driver.close();
    }
}
