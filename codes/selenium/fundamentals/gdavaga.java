// ----------------------------------------------------------------------------------------------------
// Title          : Selenium Java to maximize the browser window and get its properties
// File Name      : gdavaga.java
// Compiled       : openjdk version "21.0.8" 2025-07-15
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

class GD 
{
    public static void main(String[] args) 
    {
        System.setProperty("webdriver.chrome.driver", "/home/godarda/drivers/chromedriver");
        WebDriver driver = new ChromeDriver();
        driver.manage().window().maximize();    //maximize the browser window
        //driver.manage().window().fullscreen();
        System.out.println(driver.manage().window().getSize());
        System.out.println(driver.manage().window().getPosition());
        driver.get("https://godarda.github.io/testapp/");
        driver.close();
    }
}
