// ----------------------------------------------------------------------------------------------------
// Title          : Selenium Java to get the title of a given webpage using the getAttribute() method
// File Name      : gdzezzd.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

class GD 
{
    public static void main(String[] args) 
    {
        System.setProperty("webdriver.chrome.driver", "/home/godarda/drivers/chromedriver");
        WebDriver driver = new ChromeDriver();
        
        driver.navigate().to("https://godarda.github.io/testapp/");
        WebElement we = driver.findElement(By.tagName("title"));
        System.out.println(we.getAttribute("textContent"));
        driver.close();
    }
}
