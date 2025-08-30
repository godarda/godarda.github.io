// ----------------------------------------------------------------------------------------------------
// Title          : Selenium Java to get the present browser URL
// File Name      : gdlarzw.java
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
        driver.get("https://godarda.in/testapp/");
        String currentURL = driver.getCurrentUrl();
        System.out.println(currentURL);
        driver.close();
    }
}
